# 🧭 NicheScout

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-3776AB.svg?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110%2B-009688.svg?logo=fastapi&logoColor=white)
![Legal Data Flow](https://img.shields.io/badge/Data%20Flow-Google%20Trends%20RSS%20%2B%20Reddit%20API-success)

**NicheScout** is a market validation engine that extracts high-conviction Micro-SaaS ideas from rising search trends and public community pain points.

---

## ⚖️ Legal Data Architecture & Compliance

- **Official Feeds & APIs Only:** Uses official Google Trends RSS feeds and the official Reddit Data API (strictly public subreddit discussions, adhering to OAuth2 and rate limits).
- **Zero E-Commerce Scraping:** Never scrapes Amazon, Shopify stores, G2, or closed marketplaces.
- **Local SQLite Cache:** Persists scored niche opportunities in `nichescout_cache.db`.

---

## 📊 Sample Output

```text
Niche ID                     | Trend  | Upvotes  | Pain Hits | Validation Score
------------------------------------------------------------------------------
invoice-pdf-reconciliation   | 85     | 240      | 2         | 92.2/100
changelogs-from-git-tags     | 79     | 190      | 1         | 69.5/100
podcast-sponsor-crm          | 74     | 165      | 2         | 79.8/100
```

| Niche ID | Micro-SaaS Opportunity | Trend Index | Community Upvotes | Validation Score |
| :--- | :--- | :---: | :---: | :---: |
| `invoice-pdf-reconciliation` | Automated Multi-Currency PDF Invoice Reconciliation | 85 / 100 | 240 | **92.2 / 100** |
| `podcast-sponsor-crm` | Lightweight Sponsor Slot Booking & Ad-Read Tracker | 74 / 100 | 165 | **79.8 / 100** |
| `changelogs-from-git-tags` | Customer-Facing Release Notes Generator from Git Tags | 79 / 100 | 190 | **69.5 / 100** |

---

## 🚀 Step-by-Step Installation

```bash
git clone https://github.com/yigitozkan56/NicheScout.git
cd NicheScout
cp .env.example .env
pip install -r requirements.txt
```

---

## 💻 Usage Examples

### CLI Mode
```bash
# Discover validated Micro-SaaS niches with a score >= 65
python app.py discover --min-score 65
```

### Web Dashboard & REST API Mode
```bash
python app.py serve --port 8005
```
Open `http://127.0.0.1:8005` or `GET http://127.0.0.1:8005/api/niches`.

### Running Unit Tests
```bash
pytest tests/
```

---

## 🗺️ Roadmap

- [x] Pain-point phrase detector (`"is there a tool"`, `"tired of manually"`, `"spreadsheet hell"`)
- [x] Google Trends RSS + Reddit API composite scoring model
- [x] Local SQLite caching & FastAPI Web UI
- [ ] Export validated niche briefs to Notion / Markdown
- [ ] Subreddit velocity comparison charts
