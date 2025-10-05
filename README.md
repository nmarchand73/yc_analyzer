# YC Analyzer

Scrape and analyze Y Combinator's company directory. Includes 7,858+ companies dataset and analysis notebooks.

**What's included:**
- 🕷️ Web scraper for YC directory
- 📊 Pre-scraped dataset (Oct 2025)
- 📈 Analysis notebooks with ML models

## Quick Start

**Use pre-scraped data:**
```bash
pip install -r requirements.txt
jupyter lab
# Open: analysis/yc_comprehensive_analysis.ipynb
```

**Scrape fresh data:**
```bash
# 1. Extract URLs (~5 min)
python yc_links_extractor.py

# 2. Scrape companies (~30-60 min)
scrapy runspider scrapy-project/ycombinator/spiders/yscraper.py -o data/output.jl --loglevel=ERROR
```

## Analysis Notebooks

**`solo_founder_analysis.ipynb`** - Quick exploratory analysis
- Interactive filters
- Solo vs team comparisons
- Industry trends

**`yc_comprehensive_analysis.ipynb`** - Statistical analysis
- ML predictions with cross-validation
- Survivorship bias correction
- 20-year trends & geographic insights
- Industry saturation mapping

## Requirements

**For scraping:**
- Firefox browser
- `geckodriver` (`brew install geckodriver` on macOS)
- Python packages: `pip install -r requirements.txt`

**For analysis only:**
- Python packages: `pip install -r requirements.txt`

## Data Structure

Each company record contains 16 fields in JSON format:

```json
{
  "company_id": 31009,
  "company_name": "Bear",
  "short_description": "Show up on AI Search Engines",
  "long_description": "Bear AI helps companies show up AI search engines...",
  "batch": "Fall 2025",
  "status": "Active",
  "tags": ["generative-ai", "saas", "b2b"],
  "location": "San Francisco",
  "country": "US",
  "year_founded": 2025,
  "num_founders": 2,
  "founders_names": ["Siddhant Paliwal", "Janak Sunil"],
  "team_size": 2,
  "website": "https://usebear.ai",
  "cb_url": "",
  "linkedin_url": "https://www.linkedin.com/company/bear-ai/"
}
```

**Load data:**
```python
import pandas as pd
df = pd.read_json('data/2025-10-05-yc.companies.jl', lines=True)
```

## Key Findings

- Team-founded companies: ~3% higher success rate
- SF Bay Area: Still dominant location
- AI/ML: Fastest growing sector (recent batches)
- Statistical rigor: Survivorship bias corrected, cross-validated

---

## Credits

**Original scraper:** [Miguel Corral Jr.](https://github.com/corralm) | **Dataset:** [Kaggle](https://www.kaggle.com/datasets/miguelcorraljr/y-combinator-directory)

MIT License - See [LICENSE](./LICENSE)
