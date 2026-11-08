import pandas as pd
import numpy as np

print("--- Step 1: Loading Datasets ---")
# 1. Load the files and add a 'country' tag to keep track of where rows came from
us_df = pd.read_csv("part2_numpy_pandas/USvideos.csv")
us_df['country'] = 'US'

gb_df = pd.read_csv("part2_numpy_pandas/GBvideos.csv")
gb_df['country'] = 'GB'

in_df = pd.read_csv("part2_numpy_pandas/INvideos.csv")
in_df['country'] = 'IN'

print("--- Step 2: Combining Datasets ---")
# 2. Combine all data into a single master DataFrame
combined_df = pd.concat([us_df, gb_df, in_df], ignore_index=True)
print(f"Combined data shape: {combined_df.shape}")

print("--- Step 3: Mapping Video Categories ---")
# 3. Load the categories lookup table
categories_df = pd.read_csv("part2_numpy_pandas/categories.csv")

# 4. Merge the category names based on 'category_id'
final_df = pd.merge(combined_df, categories_df, on='category_id', how='left')

print("--- Step 4: Cleaning & Handling Missing Values ---")
# 5. Fill any missing category names with 'Unknown' using NumPy/Pandas
final_df['category_name'] = final_df['category_name'].fillna('Unknown')

# 6. Save the final cleaned master data inside the part2 folder
output_path = "part2_numpy_pandas/cleaned_trending_videos.csv"
final_df.to_csv(output_path, index=False)

print(f"\n✅ Done! Cleaned master dataset saved successfully to: {output_path}")
print(f"Final dataset preview columns: {list(final_df.columns)}")