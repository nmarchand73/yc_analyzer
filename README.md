# Y Combinator Data Scraper & Analysis

A comprehensive toolkit for scraping, analyzing, and extracting insights from the [Y Combinator companies directory](https://www.ycombinator.com/companies/). Includes data collection scripts and scientifically rigorous analysis notebooks.

**Latest Dataset:** 7,858+ YC companies (updated October 2025)

## About Y Combinator

Y Combinator is the world's most prestigious startup accelerator, having invested in over 4,000+ companies with a combined valuation exceeding $600B, including Stripe, Airbnb, Dropbox, Reddit, Coinbase, and DoorDash.

## Quick Start

**Option 1: Use Pre-scraped Data (Recommended)**

Skip the scraping and jump straight to analysis with the included dataset:

```bash
# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter lab

# Open either notebook:
# - analysis/solo_founder_analysis.ipynb (quick exploratory analysis)
# - analysis/yc_comprehensive_analysis.ipynb (rigorous statistical analysis)
```

**Option 2: Scrape Fresh Data**

Follow the [Data Collection](#data-collection) steps below to scrape the latest YC companies.

---

## Data Collection

### Requirements

**System Dependencies:**
- [Firefox](https://www.mozilla.org/en-US/firefox/new/) browser
- [geckodriver](https://github.com/mozilla/geckodriver/releases) - Install via `brew install geckodriver` (macOS) or download manually

**Python Dependencies:**
```bash
pip install -r requirements.txt
```

Core packages: `scrapy`, `selenium`, `pandas`, `tqdm`, `webdriver-manager`

### Usage Sequence

Follow these steps in order to scrape YC data:

#### Step 1: Extract Company URLs

```bash
python yc_links_extractor.py
```

**What it does:**
- Launches headless Firefox browser
- Navigates to YC companies directory
- Iterates through all batch filters (Winter 2025, Fall 2024, etc.)
- Extracts individual company URLs
- Saves URLs to `scrapy-project/ycombinator/start_urls.txt`

**Duration:** ~5-10 minutes (depending on batch count)

**Output:** List of ~8,000+ company URLs

#### Step 2: Scrape Company Data

```bash
# Basic usage (shows INFO logs)
scrapy runspider scrapy-project/ycombinator/spiders/yscraper.py -o data/output.jl --loglevel=INFO

# Quiet mode (errors only)
scrapy runspider scrapy-project/ycombinator/spiders/yscraper.py -o data/output.jl --loglevel=ERROR

# No logging
scrapy runspider scrapy-project/ycombinator/spiders/yscraper.py -o data/output.jl --nolog
```

**What it does:**
- Reads URLs from `start_urls.txt`
- Visits each company page
- Extracts structured data (see [Attributes](#attributes))
- Saves to JSON Lines format

**Duration:** ~30-60 minutes (for 8,000 companies)

**Output:** `data/output.jl` file

#### Step 3: Convert to CSV (Optional)

```bash
python json_to_csv.py
```

Converts `.jl` (JSON Lines) to `.csv` for easier Excel/Google Sheets import.

#### Step 4: Load Data for Analysis

```python
import pandas as pd

# Load JSON Lines
df = pd.read_json('data/output.jl', lines=True)

# Or load CSV
df = pd.read_csv('data/output.csv')

print(f"Loaded {len(df)} companies")
```

---

## Analysis Notebooks

Two Jupyter notebooks are included for comprehensive analysis:

### 1. Solo Founder Analysis (`analysis/solo_founder_analysis.ipynb`)

**Purpose:** Quick exploratory analysis focused on solo vs team-founded companies

**Features:**
- Interactive filters (year, industry, founder count)
- Success rate comparisons
- Industry trends visualization
- Solo founder insights

**Use case:** Fast exploration, hypothesis generation

**Limitations:** Basic statistical analysis, survivorship bias warnings included

### 2. Comprehensive Analysis (`analysis/yc_comprehensive_analysis.ipynb`)

**Purpose:** Rigorous statistical analysis with ML models

**Features:**
- **Executive dashboard:** Portfolio metrics, success rates
- **Success factor analysis:** Correlations, vintage-adjusted metrics
- **Deep solo founder analysis:** Head-to-head comparisons
- **Temporal analysis:** 20-year trends, batch evolution
- **Industry deep dive:** Saturation vs success mapping
- **Geographic intelligence:** Success by country/city
- **Advanced visualizations:** Sankey diagrams, interactive plots
- **Predictive modeling:** Logistic regression with cross-validation
- **Actionable recommendations:** Data-driven insights

**Statistical rigor:**
- ✅ Survivorship bias mitigation (filters to mature companies ≥3 years)
- ✅ Correlation vs causation warnings
- ✅ Cross-validation (5-fold)
- ✅ Class imbalance handling (ROC-AUC, balanced weights)
- ✅ Comprehensive limitations documentation

**Use case:** Publication-quality analysis, decision-making, research

---

## Project Structure

```
yc_analyzer/
├── README.md
├── LICENSE
├── requirements.txt
│
├── yc_links_extractor.py          # Step 1: Extract company URLs
├── json_to_csv.py                 # Utility: Convert .jl to .csv
│
├── scrapy-project/                # Step 2: Scrapy spider
│   └── ycombinator/
│       ├── spiders/
│       │   └── yscraper.py        # Main scraper
│       └── start_urls.txt         # Generated by Step 1
│
├── data/                          # Scraped datasets
│   └── 2025-10-05-yc.companies.jl
│
├── analysis/                      # Jupyter notebooks
│   ├── solo_founder_analysis.ipynb
│   └── yc_comprehensive_analysis.ipynb
│
└── output/                        # Generated visualizations
    └── *.png
```

## Dataset

Check out the dataset I published on [Kaggle.com](https://www.kaggle.com/datasets/miguelcorraljr/y-combinator-directory).

## Attributes

|  Attribute           |  Description | Data Type  |
|-----------------------|---|---|
| company_id            | Company id provided by YC  | int  |
| company_name          | Company name  | string  |
| short_description     | One-line description of the company  | string  |
| long_description      | Long description of the company  | string  |
| batch                 | Batch name provided by YC  | string  |
| status                | Company status  | string  |
| tags                  | Industry tags  | list  |
| location              | Company location | string  |
| country               | Company country  | string  |
| year_founded          | Year the company was founded  | int  |
| num_founders          | Number of founders  | int  |
| founders_names        | Full names of the founders  | list  |
| team_size             | Number of employees  | int  |
| website               | Company website   | string  |
| cb_url                | Company Crunchbase url  | string  |
| linkedin_url          | Company LinkedIn url  | string  |

## Sample Data

Note: I excluded 'short_description', 'long_description', 'cb_url', and 'linkedin_url'  in the sample data for brevity.

| company_id | company_name | short_description                         | batch | status   | tags                                                      | location      | country | year_founded | num_founders | founders_names                                       | team_size | website                  |   |
|------------|--------------|-------------------------------------------|-------|----------|-----------------------------------------------------------|---------------|---------|--------------|--------------|------------------------------------------------------|-----------|--------------------------|---|
| 240        | Stripe       | Economic infrastructure for the internet. | S09   | Active   | ['Fintech', 'Banking as a Service', 'SaaS']               | San Francisco | US      |              | 2            | ['John Collison', 'Patrick Collison']                | 7000      | <http://stripe.com>        |   |
| 271        | Airbnb       | Book accommodations around the world.     | W09   | Public   | ['Travel', 'Marketplace']                                 | San Francisco | US      | 2008         | 3            | ['Nathan Blecharczyk', 'Brian Chesky', 'Joe Gebbia'] | 6132      | <http://airbnb.com>        |   |
| 325        | Dropbox      | Backup and share files in the cloud.      | S07   | Public   | []                                                        | San Francisco | US      | 2008         | 2            | ['Arash Ferdowsi', 'Drew Houston']                   | 4000      | <http://dropbox.com>       |   |
| 379        | Reddit       | The frontpage of the internet.            | S05   | Acquired | ['Community', 'Social', 'Social Media', 'Social Network'] | San Francisco | US      |              | 1            | ['Steve Huffman']                                    | 201       | <http://reddit.com>        |   |
| 439        | Coinbase     | Buy, sell, and manage cryptocurrencies.   | S12   | Public   | ['Crypto / Web3']                                         | San Francisco | US      | 2012         | 1            | ['Brian Armstrong']                                  | 6112      | <https://www.coinbase.com> |   |
| 531        | DoorDash     | Restaurant delivery.                      | S13   | Public   | ['E-commerce', 'Marketplace']                             | San Francisco | US      | 2013         | 3            | ['Andy Fang', 'Stanley Tang', 'Tony Xu']             | 8600      | <http://doordash.com>      |   |

---

## Key Insights from Analysis

Based on analysis of 7,858+ YC companies:

**Success Factors:**
- Team-founded companies show ~2-3pp higher success rates than solo founders
- Company age, team size, and B2B focus correlate positively with exits
- SF Bay Area still dominates, but international presence is growing
- AI/ML companies experiencing explosive growth in recent batches

**Methodology:**
- Success = Public or Acquired status
- Analysis filters to "mature" companies (≥3 years old) to reduce survivorship bias
- Statistical rigor: correlation warnings, cross-validation, comprehensive limitations

**For detailed findings:** See analysis notebooks

---

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests if applicable
4. Submit a pull request

**Areas for contribution:**
- Additional analysis notebooks
- Data quality improvements
- Scraper enhancements for new YC features
- Statistical method improvements

---

## License

Distributed under the MIT license. See [LICENSE](./LICENSE) for more information.

---

## Credits

**Original Scraper:** [Miguel Corral Jr.](https://github.com/corralm)
**Analysis & Enhancements:** Enhanced with comprehensive statistical analysis and Jupyter notebooks

**Dataset:** Also available on [Kaggle.com](https://www.kaggle.com/datasets/miguelcorraljr/y-combinator-directory)
