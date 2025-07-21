import pandas as pd

def summarize_mentions(csvfile, out_md):
    df = pd.read_csv(csvfile)
    top_keywords = df['keyword'].value_counts()
    # Simple SWOT logic; refine as needed for context
    strengths = top_keywords[top_keywords.index.isin(['party','adventure','local','instagrammable'])].to_dict()
    weaknesses = top_keywords[top_keywords.index.isin(['wifi','safety'])].to_dict()
    opportunities = top_keywords[top_keywords.index.isin(['eco','solo','group','event'])].to_dict()
    threats = top_keywords[top_keywords.index.isin(['review'])].to_dict()
    with open(out_md, 'w') as f:
        f.write("# SWOT Analysis\n\n")
        f.write("## Strengths\n")
        for k, v in strengths.items():
            f.write(f"- {k.title()}: {v} mentions\n")
        f.write("\n## Weaknesses\n")
        for k, v in weaknesses.items():
            f.write(f"- {k.title()}: {v} mentions\n")
        f.write("\n## Opportunities\n")
        for k, v in opportunities.items():
            f.write(f"- {k.title()}: {v} mentions\n")
        f.write("\n## Threats\n")
        for k, v in threats.items():
            f.write(f"- {k.title()}: {v} mentions\n")

# Usage example
summarize_mentions("output/mentions_instagram_winter.csv", "output/swot_winter.md")
summarize_mentions("output/mentions_instagram_summer.csv", "output/swot_summer.md")
