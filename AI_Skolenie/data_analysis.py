from openai import OpenAI
import csv

client = OpenAI()

# Read CSV file
csv_file_path = r"C:\Users\student\PD_Student\user_data4.csv"

# Read CSV data
with open(csv_file_path, 'r') as file:
    csv_content = file.read()

# Count rows for context
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    row_count = sum(1 for row in csv_reader) - 1  # Subtract header row

# Prepare prompt for LLM
prompt = f"""Please analyze the following CSV dataset containing {row_count} user records.

CSV Data:
{csv_content}

Please provide:
1. A summary of the dataset structure and key columns
2. Basic statistics (e.g., age distribution, gender breakdown, country distribution)
3. Any interesting patterns or insights you notice
4. Data quality observations (missing values, outliers, etc.)
5. Recommendations for further analysis

Keep your analysis clear and concise."""

# Send to LLM for analysis
print("Analyzing CSV data with LLM...")
print("-" * 80)

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

# Print the analysis
print(response.output_text)
print("-" * 80)
print(f"\nAnalysis completed for {row_count} records from {csv_file_path}")