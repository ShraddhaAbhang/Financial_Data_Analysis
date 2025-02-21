import pandas as pd
import matplotlib.pyplot as plt
import os

# Define file path
INPUT_FILE = "../Data/Extracted/financial_summary.csv"

# Load extracted financial data
df = pd.read_csv(INPUT_FILE)

# Convert financial values to numeric (handling missing values)
columns_to_convert = ["Total Revenue", "Net Income", "Total Assets", "Total Liabilities", "Cash Flow from Operating Activities"]
for col in columns_to_convert:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Extract company names from source file names
df["Company"] = df["Source"].apply(lambda x: "Microsoft" if "msft" in x.lower() else 
                                             "Tesla" if "tsla" in x.lower() else 
                                             "Apple" if "aapl" in x.lower() else "Unknown")

# Extract year from source file names
df["Year"] = df["Source"].str.extract(r'(\d{4})')

# Convert Year to integer
df["Year"] = pd.to_numeric(df["Year"], errors='coerce')

# Sort values by Company and Year
df = df.sort_values(by=["Company", "Year"])

# Save cleaned data
df.to_csv("../Data/Extracted/cleaned_financial_data.csv", index=False)

# Plot trends for each metric
metrics = ["Total Revenue", "Net Income", "Total Assets", "Total Liabilities", "Cash Flow from Operating Activities"]

for metric in metrics:
    plt.figure(figsize=(10, 5))
    for company in df["Company"].unique():
        company_df = df[df["Company"] == company]
        plt.plot(company_df["Year"], company_df[metric], marker='o', label=company)

    plt.xlabel("Year")
    plt.ylabel(metric)
    plt.title(f"{metric} Trends (Last 3 Years)")
    plt.legend()
    plt.grid()
    plt.savefig(f"../Reports/{metric}_trend.png")  # Save each trend plot
    plt.show()

print("✅ Trend analysis completed! Check the Reports folder for visualizations.")
