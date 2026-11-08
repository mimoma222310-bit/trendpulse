# TrendPulse: YouTube Trending Video Data Analytics

This repository contains a full four-part analytical workflow exploring daily trending YouTube video datasets across the US, UK, and India, gathering over 46,000 unique records.

## Project Structure
* **`part1_python_foundations/`** - Raw file-handling parser utilizing native Python dictionaries, loops, and file operations.
* **`part2_numpy_pandas/`** - Data cleaning, manipulation, and merging system to cross-reference numeric keys with string category mappings.
* **`part3_visualization_eda/`** - Graphical trend exploratory systems analyzing video interaction properties across categories.
* **`part4_sql_spreadsheet/`** - In-memory SQLite analytics compilation generating target summary views for reporting metrics.

## Setup and Running Instructions
1. Ensure `pandas`, `numpy`, `matplotlib`, and `seaborn` are installed:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
2. Execute each analytical stage inside the project from your root directory:
   ```bash
   python part1_python_foundations/pure_python_parser.py
   python part2_numpy_pandas/process_data.py
   python part3_visualization_eda/visualization.py
   python part4_sql_spreadsheet/sql_queries.py
   ```