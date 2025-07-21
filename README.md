# Curiocity Social Media SWOT Repo
<<<<<<< HEAD
=======

## Purpose

Automate collection, filtering, and SWOT-ready analysis of Instagram and TikTok posts about hostels in South Africa by season, focusing on keywords aligned with 18–35 year-old guest priorities. This enables the Curiocity team to make informed marketing, content, and product decisions based on real traveler sentiment and trends for both winter and summer.

## Requirements

* Python 3.7+
* pip (`pip install -r requirements.txt`)
* Node.js and npm (for TikTok-scraper: [https://nodejs.org/en/download/](https://nodejs.org/en/download/))
* TikTok-scraper (`npm install -g tiktok-scraper`)
* Instaloader (installed via requirements.txt)

After you install TikTok-scraper globally, (with `npm install -g tiktok-scraper`), proceed as follows:

Clone or download this repo and `cd` into the folder. Install all Python dependencies using:

```sh
pip install -r requirements.txt
```

If you do not have Node.js, download and install it from [https://nodejs.org/en/download/](https://nodejs.org/en/download/).

(Optional) Configure hashtags and keywords:
Edit `config/hashtags_by_season.json` to update which hashtags are monitored for each season.
If you want to add or remove keywords for sentiment/theme detection, edit the `KEYWORDS` list in `process_data.py`.

Collect Instagram and TikTok data by season:
For Instagram, run:

```sh
bash collect_instagram.sh winter
bash collect_instagram.sh summer
```

For TikTok, run:

```sh
bash collect_tiktok.sh winter
bash collect_tiktok.sh summer
```

Data will be saved in `data/instagram/[season]/` and `data/tiktok/[season]/`.

Process data and extract keyword matches:
Run:

```sh
python process_data.py
```

This will create filtered CSVs in `output/` with all posts/comments containing relevant keywords for each platform and season.

Generate SWOT analysis:
Run:

```sh
python analyze_swot.py
```

This will output two markdown SWOT reports (`swot_winter.md`, `swot_summer.md`) and a comprehensive CSV of all matched mentions in the `output/` folder.

Review, present, and apply insights:
Open the markdown SWOTs in `/output/` for strategic strengths, weaknesses, opportunities, and threats as seen by real travelers.
Use the CSVs to dive deeper into specific posts or topics.
Plug insights into your marketing decks, site copy updates, campaign planning, or team presentations.

If you see npm deprecation warnings:
These are normal for social media scrapers. Only take action if you get a red “ERR!” and TikTok-scraper fails to run.

API rate limits:
Instagram and TikTok may block or slow down repeated scraping. Run scripts at different times or in smaller batches if you hit errors.

Permission errors:
On Mac/Linux, try `sudo npm install -g tiktok-scraper`. On Windows, use “Run as administrator”.

Want to analyze different hashtags or keywords?
Edit `config/hashtags_by_season.json` and `KEYWORDS` in `process_data.py` to match your strategy or test new themes.

Python errors:
Check you’re running Python 3.7+ and all dependencies from `requirements.txt` are installed.

Full analysis checklist:

* Install requirements and confirm all scripts run from your terminal.
* (Optionally) adjust hashtags/keywords for your season or campaign.
* Scrape data for both Instagram and TikTok for each season.
* Process and filter posts by strategy-driven keywords.
* Generate SWOT reports and summary CSVs.
* Use these for strategic planning, proposal writing, and team alignment—repeat seasonally or for major campaign launches.

For errors, improvements, or further guidance, contact your digital strategy lead or the repo maintainer.
>>>>>>> 9b941e21060d58a8cc3eed11dc59f4047c203004
