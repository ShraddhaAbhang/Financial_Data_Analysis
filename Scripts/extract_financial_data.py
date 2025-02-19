import pdfplumber
import pandas as pd
import os

# Define paths
RAW_DATA_DIR = "../Data/Raw/"
EXTRACTED_DATA_DIR = "../Data/Extracted/"

# Ensure the extracted data folder exists
os.makedirs(EXTRACTED_DATA_DIR, exist_ok=True)

# List of PDF files (Update with actual filenames)
pdf_files = {
    "Microsoft": "microsoft_10k.pdf",
    "Tesla": "tesla_10k.pdf",
    "Apple": "apple_10k.pdf",
}

# Function to extract tables from PDF
def extract_tables_from_pdf(pdf_path):
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted_tables = page.extract_tables()
            for table in extracted_tables:
                tables.append(pd.DataFrame(table))  # Convert each table to a DataFrame
    return tables

# Process each company's 10-K PDF
for company, pdf_file in pdf_files.items():
    pdf_path = os.path.join(RAW_DATA_DIR, pdf_file)

    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        continue

    print(f"Extracting tables from {company}...")
    extracted_tables = extract_tables_from_pdf(pdf_path)

    # Save extracted tables as CSV
    for i, table in enumerate(extracted_tables):
        table.dropna(how="all", axis=1, inplace=True)  # Remove empty columns
        table.dropna(how="all", axis=0, inplace=True)  # Remove empty rows
        csv_filename = f"{company}_table_{i+1}.csv"
        table.to_csv(os.path.join(EXTRACTED_DATA_DIR, csv_filename), index=False)
        print(f"Saved table {i+1} for {company} as {csv_filename}")

print("✅ Extraction Complete!")
