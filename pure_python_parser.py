print("--- Part 1: Pure Python File Parser ---")

file_path = "part2_numpy_pandas/categories.csv"
category_counts = 0

# Open and parse the file line by line without using pandas
try:
    with open(file_path, "r", encoding="utf-8") as file:
        # Read lines
        lines = file.readlines()
        
        print("\nParsing raw categories data:")
        for line in lines[1:6]: # Print just the first 5 category rows
            cleaned_line = line.strip()
            print(f"-> Raw Row Found: {cleaned_line}")
            category_counts += 1
            
    print(f"\n✅ Pure Python check finished! Successfully read rows cleanly.")
except FileNotFoundError:
    print("⚠️ Raw data categories file not found at the checked path.")