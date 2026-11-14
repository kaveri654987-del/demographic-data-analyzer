# Demographic Data Analyzer

A Python data-analysis project that uses **Pandas** to explore demographic data from the 1994 U.S. Census.

## Project objectives

This program calculates:
- The number of people represented in each race category
- The average age of men
- The percentage of people with a Bachelor's degree
- The percentage of people with and without advanced education who earn more than $50K
- The minimum number of hours worked per week
- The percentage of minimum-hour workers who earn more than $50K
- The country with the highest percentage of people earning more than $50K
- The most common occupation among people earning more than $50K in India

Average and percentage results are rounded to one decimal place.

## Technologies
- Python 3
- Pandas

## Project files
```text
demographic-data-analyzer/
├── demographic_data_analyzer.py
├── requirements.txt
└── README.md
```

## Setup and run

1. Download the `adult.data.csv` dataset from the freeCodeCamp Demographic Data Analyzer project resources and place it in the same folder as the Python file.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run:
   ```bash
   python demographic_data_analyzer.py
   ```

**Note:** The dataset is not included in this repository. Add `adult.data.csv` locally before running the program.

## Main function

`calculate_demographic_data(print_data=True)` prints the analysis and returns the results in a dictionary.
