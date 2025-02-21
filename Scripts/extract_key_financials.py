import pandas as pd
import os

# Define paths
EXTRACTED_DATA_DIR = "../Data/Extracted/"
OUTPUT_FILE = "../Data/Extracted/financial_summary.csv"

# Keywords to identify financial metrics in tables
financial_keywords = {
    "Total Revenue": ["total revenue", "revenues", "net sales"],
    "Net Income": ["net income", "net earnings", "profit"],
    "Total Assets": ["total assets"],
    "Total Liabilities": ["total liabilities"],
    "Cash Flow from Operating Activities": ["cash provided by operating", "net cash from operating"]
}

# Function to search for financial metrics in extracted tables
def extract_financial_values(file_path):
    df = pd.read_csv(file_path, header=None)
    extracted_values = {}

    for metric, keywords in financial_keywords.items():
        for col in df.columns:
            for row in df[col].astype(str):
                row_lower = row.lower()
                if any(keyword in row_lower for keyword in keywords):
                    try:
                        value = df.iloc[df[df[col] == row].index[0], col + 1]
                        extracted_values[metric] = value
                    except:
                        continue
    return extracted_values

# Process each extracted table
financial_data = []

for file in os.listdir(EXTRACTED_DATA_DIR):
    if file.endswith(".csv"):
        file_path = os.path.join(EXTRACTED_DATA_DIR, file)
        print(f"Processing: {file}")
        extracted_values = extract_financial_values(file_path)
        if extracted_values:
            extracted_values["Source"] = file
            financial_data.append(extracted_values)

# Convert results to a DataFrame
df_summary = pd.DataFrame(financial_data)

# Save extracted financial data
df_summary.to_csv(OUTPUT_FILE, index=False)
print(f"✅ Financial summary saved at: {OUTPUT_FILE}")
