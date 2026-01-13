import pandas as pd

def analyze_data(file_path):
    """
    Performs basic data analysis on the user data CSV file.
    Calculates min, max, average, and median salary.
    Generates a markdown report.
    """
    try:
        # Read the CSV file
        df = pd.read_csv(file_path, encoding='latin1')

        # Ensure 'salary' column exists
        if 'salary' not in df.columns:
            return "Error: 'salary' column not found in the CSV file."

        # Calculate statistics
        min_salary = df['salary'].min()
        max_salary = df['salary'].max()
        avg_salary = df['salary'].mean()
        median_salary = df['salary'].median()

        # Generate markdown report
        report = f"""# User Data Analysis Report

## Salary Statistics

| Metric   | Value      |
|----------|------------|
| Minimum  | ${min_salary:,.2f} |
| Maximum  | ${max_salary:,.2f} |
| Average  | ${avg_salary:,.2f} |
| Median   | ${median_salary:,.2f} |
"""

        # Write report to user_analysis.md
        with open('user_analysis.md', 'w') as f:
            f.write(report)

        return "Successfully generated user_analysis.md"

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    result = analyze_data('user_data4.csv')
    print(result)
