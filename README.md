# YC Companies: Scraper & AI Analysis

**Scrape YC data and transform it into actionable startup intelligence** - Get insights, predictions, and recommendations for founders, investors, and researchers.

## 🚀 What This Does

**1. Scrapes YC Data** - Automatically collects company information from Y Combinator
**2. Analyzes 5,463+ companies** across 20 years to answer:
- **What makes startups successful?**
- **Which industries are growing fastest?**
- **How do solo founders compare to teams?**
- **Where are the best opportunities?**
- **What's the success probability for any company?**

## 🎯 Key Features

### **🕷️ Data Scraping**
- **Automated Collection** - Scrapes YC companies directory automatically
- **Real-time Updates** - Gets latest company information
- **Batch Processing** - Handles large-scale data collection
- **Data Validation** - Ensures data quality and completeness

### **📊 Data Analysis**
- **Portfolio Overview** - Success rates, founder types, geographic distribution
- **Success Factors** - What correlates with startup success
- **Industry Trends** - Which sectors are growing fastest
- **Geographic Insights** - Where successful companies are located
- **Predictive Models** - Success probability for any company

### **🧠 AI Intelligence**
- **Company Profiling** - Automatic categorization and archetype detection
- **Market Opportunities** - AI-powered trend detection
- **Success Narratives** - Why companies succeed (AI-generated insights)
- **Competitive Analysis** - Automated landscape analysis
- **Personalized Recommendations** - Tailored advice for founders

### **📈 Interactive Tools**
- **Year-by-Year Analysis** - Compare different YC batches
- **Interactive Dashboards** - Explore data with filters and visualizations
- **AI Chat Interface** - Ask questions in natural language
- **Company Deep Dives** - Analyze specific companies with AI

## 📊 Key Findings

### **What Makes Startups Successful**
- **Company Age** is the #1 predictor (older companies succeed more)
- **Team Growth** - 87% of successful solo founders build teams
- **Location** - SF Bay Area companies outperform others
- **Industry Timing** - AI/ML companies are exploding (47.8% of recent batches)
- **Founder Type** - Teams generally beat solo founders

### **Market Trends**
- **AI/ML** is the fastest-growing sector
- **B2B SaaS** remains the most successful category  
- **International** - 31.8% of companies are non-US
- **Solo Decline** - From 39% (early) to 17% (recent batches)
- **Success Rate** - 13.1% overall (public/acquired)

## 🚀 Quick Start

### **1. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **2. Scrape YC Data**
```bash
# Step 1: Extract company URLs (requires Firefox/Chrome)
python yc_links_extractor.py

# Step 2: Run the scraper
cd scrapy-project
scrapy crawl YCombinatorScraper

# Output will be saved to data/yc_companies.jl
```

### **3. Set Up OpenAI API (Optional)**
```bash
export OPENAI_API_KEY='your-key-here'
```

### **4. Run the Analysis**
```python
# Open the analysis notebook
jupyter lab analysis/genai_enhanced_analysis.ipynb

# Or run specific analyses
python -c "from analysis.genai_enhanced_analysis import *; create_executive_summary()"
```

### **5. Try These Examples**
```python
# Get portfolio overview
create_executive_summary()

# Analyze a specific year
quick_year_analysis(2023)

# Get AI insights for a company
analyze_company_interactive(company_name='Airbnb')

# Market intelligence
quick_market_analysis()

# Personalized recommendations
get_personalized_recommendations(founder_type='solo', industry='AI')
```

## 🕷️ Data Scraping

### **Step 1: Extract Company URLs**
```bash
# First, extract all company URLs from YC website
python yc_links_extractor.py

# This will create scrapy-project/ycombinator/start_urls.txt
# with all company URLs for scraping
```

### **Step 2: Run the Scraper**
```bash
# Navigate to scraper directory
cd scrapy-project

# Run the scraper
scrapy crawl YCombinatorScraper

# Output will be saved to data/yc_companies.jl
```

### **Complete Scraping Workflow**
```bash
# 1. Extract URLs (requires Firefox/Chrome)
python yc_links_extractor.py

# 2. Run the scraper
cd scrapy-project
scrapy crawl YCombinatorScraper

# 3. Check output
ls -la data/yc_companies.jl
```

### **Advanced Scraping Options**
```bash
# Custom output file
scrapy crawl YCombinatorScraper -s FEEDS='data/custom_companies.jl'

# Limit number of companies
scrapy crawl YCombinatorScraper -s CLOSESPIDER_PAGECOUNT=100

# Run with custom settings
scrapy crawl YCombinatorScraper -s DOWNLOAD_DELAY=1 -s RANDOMIZE_DOWNLOAD_DELAY=0.5
```

### **Scraping Configuration**
```python
# Customize scraping in scrapy-project/ycombinator/settings.py
DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = 0.5
CONCURRENT_REQUESTS = 16
ROBOTSTXT_OBEY = True
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
```

### **Troubleshooting Scraping**
```bash
# If URL extraction fails:
# 1. Check Firefox is installed
# 2. Update webdriver-manager: pip install --upgrade webdriver-manager
# 3. Check internet connection

# If scraper fails:
# 1. Check start_urls.txt exists and has URLs
# 2. Verify scrapy is installed: pip install scrapy
# 3. Check robots.txt compliance

# Common issues:
# - "GeckoDriver not found": webdriver-manager will auto-install
# - "No URLs found": Check YC website structure hasn't changed
# - "Rate limited": Increase DOWNLOAD_DELAY in settings.py
```

## 📖 How to Use

### **For Founders**
```python
# Get personalized recommendations
get_personalized_recommendations(
    founder_type='solo', 
    industry='AI', 
    location='San Francisco'
)

# Analyze your company
analyze_company_interactive(company_name='Your Company')
```

### **For Investors**
```python
# Market intelligence
quick_market_analysis()

# Year-by-year trends
quick_year_analysis(2023)

# Success probability
model_results = build_production_ready_model(enhanced_df)
```

### **For Researchers**
```python
# Success factor analysis
analyze_success_factor('company_age', 'Company Age Impact')

# Industry trends
analyze_industry_trends()

# Geographic insights
create_geographic_dashboard()
```

## 🔧 Requirements

### **System Requirements**
- **Python 3.8+**
- **8GB+ RAM** (16GB recommended)
- **Chrome/Chromium** (for web scraping)
- **OpenAI API Key** (for AI features - optional)

### **Installation**
```bash
# Clone the repository
git clone https://github.com/your-repo/yc-scraper.git
cd yc-scraper

# Install dependencies
pip install -r requirements.txt

# Set up OpenAI API (optional)
export OPENAI_API_KEY='your-key-here'
```

### **Scraping Requirements**
- **Firefox browser** (for URL extraction)
- **GeckoDriver** (automatically installed via webdriver-manager)
- **Stable internet connection** for data collection
- **Sufficient disk space** for data storage
- **Respectful scraping** - follows robots.txt and rate limits

### **Cost**
- **OpenAI API**: ~$0.05-0.15 per company analysis (optional)
- **Free features**: Most analysis works without API key
- **Scraping**: Free (just requires time and bandwidth)

## 📊 Data & Methodology

### **Dataset**
- **5,463+ companies** across 20 years (2005-2025)
- **Success Rate**: 13.1% (public/acquired)
- **Geographic Coverage**: Global (31.8% international)
- **Industry Coverage**: All sectors with AI/ML focus

### **Analysis Approach**
- **Survivorship Bias Mitigation**: Focus on mature companies (≥3 years)
- **Statistical Rigor**: Proper correlation analysis and significance testing
- **AI Enhancement**: GPT-4 for insights and narratives
- **Production Ready**: Multiple ML algorithms with ensemble methods

### **Limitations**
- **Correlation ≠ Causation** - All insights are correlational
- **Selection Bias** - YC companies are pre-selected (top 1-2% of applicants)
- **Missing Data** - Some companies have incomplete information
- **Past Performance ≠ Future Results** - Historical patterns may not persist

## 🎯 Who This Is For

### **Founders**
- Understand success patterns
- Get personalized recommendations
- Identify market opportunities
- Learn from successful companies

### **Investors**
- Analyze portfolio trends
- Identify promising sectors
- Geographic opportunity mapping
- Success probability assessment

### **Researchers**
- Academic research support
- Statistical analysis tools
- Data visualization capabilities
- Methodological frameworks

## 📄 License & Contributing

- **Open Source**: MIT License
- **Contributing**: All contributions welcome
- **Issues**: Report bugs or request features
- **Documentation**: Comprehensive notebook documentation

---

**🚀 Ready to analyze YC data and get actionable insights!**

*Start with the Quick Start section above to get running in minutes.*