Step-by-Step Instructions for Running Curiocity Social Media SWOT Analysis

Step 1: Clone the Repository

Open Terminal (Mac/Linux) or Command Prompt (Windows).

Navigate to the folder where you want the project.

Run:

git clone https://github.com/yourorg/curiocity_social_media_swot.git
cd curiocity_social_media_swot

Step 2: Install Python Requirements

Make sure you have Python 3.7+ installed.

In the terminal, run:

pip install -r requirements.txt

Wait until all packages install successfully.

Step 3: Install Node.js and npm (if not already installed)

Go to: https://nodejs.org/en/download/

Download and install the LTS version for your OS.

Confirm installation:

node -v
npm -v

Step 4: Install TikTok-Scraper Globally

In terminal, run:

npm install -g tiktok-scraper

If you get permission errors, try:

sudo npm install -g tiktok-scraper

Confirm it works:

tiktok-scraper --help

Step 5: Configure Hashtag Input (Optional)

Open config/hashtags_by_season.json in a code editor.

Add or edit hashtags for "winter" and "summer".

Save the file.

Step 6: Scrape Instagram Data

In terminal, run:

bash collect_instagram.sh winter
bash collect_instagram.sh summer

Wait for each to complete. Output appears in data/instagram/[season]/

Step 7: Scrape TikTok Data

In terminal, run:

bash collect_tiktok.sh winter
bash collect_tiktok.sh summer

Files will appear in data/tiktok/[season]/

Step 8: Process Collected Data

In terminal, run:

python process_data.py

This creates filtered CSVs in output/, with keyword-matched content for both platforms and seasons.

Step 9: Generate SWOT Reports

In terminal, run:

python analyze_swot.py

Output files (swot_winter.md, swot_summer.md, and all_mentions.csv) will appear in the output/ folder.

Step 10: Review and Use the Results

Open markdown SWOT files using any markdown viewer or text editor.

Open all_mentions.csv in Excel or Google Sheets for full post context.

Insert insights into your marketing strategy, content roadmap, or stakeholder presentations.

Step 11: Convert Data to a Queryable Database

Create a SQLite, PostgreSQL, or MySQL database to house all all_mentions.csv data.

Use a script like:

import pandas as pd
import sqlite3
conn = sqlite3.connect('curiocity_insights.db')
df = pd.read_csv('output/all_mentions.csv')
df.to_sql('mentions', conn, if_exists='replace', index=False)

Enable text search capabilities:

CREATE VIRTUAL TABLE mentions_fts USING fts5(content);
INSERT INTO mentions_fts (rowid, content) SELECT rowid, comment FROM mentions;

Query by keyword, sentiment, platform, season, or location using SQL.

Build dashboards in Google Data Studio, Tableau, or Superset for visualization.

Recommendations for Strategic Impact Measurement

Tag each mention with its likely conversion phase (awareness, interest, decision).

Add UTM-tagged links in social content to track post-level conversions in GA4.

Track bookings from UGC-referenced campaigns using custom links or promo codes.

Integrate social data with booking logs from Curiocity’s PMS to attribute revenue.

Perform cohort analysis: compare periods with/without influencer campaigns or social UGC boosts.

Use keyword frequency over time to monitor brand sentiment and experience appeal shifts.

Troubleshooting

TikTok-scraper fails: Use Docker version or contact support.

Rate limits: Wait and retry after 1-2 hours.

CSV is empty: Ensure hashtags return active public posts.

You're now ready to deliver season-specific social media SWOT insights for Curiocity and turn that data into a continuously queryable, trackable, and measurable asset aligned with long-term growth.
