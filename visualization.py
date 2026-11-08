import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("--- Step 1: Loading Cleaned Dataset ---")
df = pd.read_csv("part2_numpy_pandas/cleaned_trending_videos.csv")
sns.set_theme(style="whitegrid")

print("--- Step 2: Generating Engagement Plots ---")

# Plot 1: Top Categories by Views
plt.figure(figsize=(12, 6))
category_views = df.groupby('category_name')['views'].median().sort_values(ascending=False).head(10)
sns.barplot(x=category_views.values, y=category_views.index, palette="viridis")
plt.title('Top 10 Video Categories by Median Views')
plt.xlabel('Median Views')
plt.ylabel('Category Name')
plt.tight_layout()
plt.savefig('part3_visualization_eda/top_categories_views.png')
plt.close()

# Plot 2: Relationship Between Likes and Views
plt.figure(figsize=(10, 6))
sample_df = df.sample(n=min(5000, len(df)), random_state=42)
sns.scatterplot(data=sample_df, x='views', y='likes', alpha=0.5, hue='country')
plt.title('Views vs. Likes Distribution (Sampled)')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.tight_layout()
plt.savefig('part3_visualization_eda/views_vs_likes.png')
plt.close()

print("\n✅ Success! Saved visual trend charts inside 'part3_visualization_eda/' folder.")