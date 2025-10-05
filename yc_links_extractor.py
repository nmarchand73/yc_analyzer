import json
import re
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.firefox import GeckoDriverManager
from tqdm import tqdm
    
# Create the driver after it's needed, not at module level
page = "https://www.ycombinator.com/companies"


def make_driver():
    """Creates headless Firefox WebDriver instance."""
    firefox_options = Options()
    firefox_options.add_argument('-headless')
    
    # Create the service with the local geckodriver path
    service = FirefoxService(GeckoDriverManager().install())

    #service = FirefoxService(executable_path=r'C:\Users\Nicolas.Marchand\Documents\DEV\PROJECTS\YC_SCRAPER\gecko_driver\geckodriver.exe')
    
    # Set timeout to a specific number to avoid the object reference issue
    driver = webdriver.Firefox(
        service=service,
        options=firefox_options
    )
    
    # Set page load timeout explicitly
    driver.set_page_load_timeout(30)
    
    return driver



def get_page_source(driver):
    """Returns the source of the current page."""
    driver.get(page)


def click_see_all_options(driver):
    """Clicks 'See all options' button to load checkboxes for all batches."""
    sleep(3)
    try:
        see_all_options = driver.find_element(By.LINK_TEXT, 'See all options')
        see_all_options.click()
    except Exception as e:
        print(f"Could not find 'See all options': {e}")


def compile_batches(driver):
    """Returns elements of checkboxes from all batches."""
    # Updated pattern to match new YC website format: "Winter 2025", "Summer 2024", etc.
    pattern = re.compile(r'^(Winter|Summer|Spring|Fall|W|S|IK)\s*\d{4}')
    bx = driver.find_elements(By.XPATH, '//label')
    print(f"Found {len(bx)} label elements")
    matched_batches = []
    for element in bx:
        if pattern.match(element.text):
            matched_batches.append(element)
            yield element
    print(f"Matched {len(matched_batches)} batch elements")


def scroll_to_bottom(driver):
    """Scrolls to the bottom of the page."""

    # get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # scroll down to bottom
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # wait to load page
        sleep(3)

        # calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def fetch_url_paths(driver):
    """Returns a generator with url paths for all companies."""
    # contains 'companies' but not 'founders'
    elements = driver.find_elements(
        By.XPATH, ('//a[contains(@href,"/companies/") and not(contains(@href,"founders"))]'))
    for url in elements:
        yield url.get_attribute('href')


def write_urls_to_file(ul: list):
    """Appends a list of company urls to a file."""
    with open('./scrapy-project/ycombinator/start_urls.txt', 'w') as f:
        json.dump(ul, f)


def yc_links_extractor():
    """Run the main script to write all start urls to a file."""
    driver = make_driver()
    print(f"Attempting to scrape links from {page}.")
    get_page_source(driver)
    click_see_all_options(driver)
    # compile an array of batches (checkbox elements)
    batches = compile_batches(driver)
    ulist = []

    for b in tqdm(list(batches)):
        # filter companies
        b.click()

        # scroll down to load all companies
        scroll_to_bottom(driver)

        # fetch links and append them to ulist
        urls = [u for u in fetch_url_paths(driver)]
        ulist.extend(urls)

        # uncheck the batch checkbox
        b.click()
    
    write_urls_to_file(ulist)
    driver.quit()


if __name__ == '__main__':

    yc_links_extractor()
