import pandas as pd
import sqlite3

print("--- Step 1: Loading Data into SQL Database ---")
# Load our cleaned data master file
df = pd.read_csv("part2_numpy_pandas/cleaned_trending_videos.csv")

# Create a local, temporary SQL database file in memory
conn = sqlite3.connect(":memory:")

# Store the data frame inside an SQL table named 'trending_videos'
df.to_sql("trending_videos", conn, index=False, if_exists="replace")

print("--- Step 2: Running Analytics Queries ---")

# Query A: Summary metrics by country
query_country = """
SELECT 
    country,
    COUNT(*) as total_trending_videos,
    ROUND(AVG(views), 0) as average_views,
    ROUND(AVG(likes), 0) as average_likes
FROM trending_videos
GROUP BY country;
"""

# Query B: Top 5 trending categories overall
query_categories = """
SELECT 
    category_name,
    COUNT(*) as video_count,
    SUM(views) as total_category_views
FROM trending_videos
GROUP BY category_name
ORDER BY video_count DESC
LIMIT 5;
"""

print("\n📊 [SQL RESULT A] Performance Metrics by Country:")
country_results = pd.read_sql_query(query_country, conn)
print(country_results.to_string(index=False))

print("\n📊 [SQL RESULT B] Top 5 Most Frequent Trending Categories:")
category_results = pd.read_sql_query(query_categories, conn)
print(category_results.to_string(index=False))

# Export the SQL summary data out directly to a clear spreadsheet report
output_excel = "part4_sql_spreadsheet/executive_briefing_metrics.csv"
country_results.to_csv(output_excel, index=False)
print(f"\n✅ Done! Summary report metrics successfully exported to: {output_excel}")

conn.close()