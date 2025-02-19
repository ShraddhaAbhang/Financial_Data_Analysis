import os

# Define the folder structure
folder_structure = {
    "Financial_Data_Analysis": [
        "env",  # Virtual environment (optional)
        "Data/Raw",  # Store raw downloaded 10-K PDFs
        "Data/Extracted",  # Store extracted financial data (CSV, JSON)
        "Notebooks",  # Jupyter notebooks for analysis
        "Reports",  # Final reports and insights
        "Scripts",  # Python scripts for automation
    ]
}

# Create directories
for root, subdirs in folder_structure.items():
    for subdir in subdirs:
        path = os.path.join(root, subdir)
        os.makedirs(path, exist_ok=True)
        print(f"Created: {path}")

# Create empty files
files_to_create = [
    "Financial_Data_Analysis/requirements.txt",
    "Financial_Data_Analysis/main.py"
]

for file_path in files_to_create:
    with open(file_path, "w") as f:
        pass
    print(f"Created: {file_path}")

print("\n✅ Project structure setup complete!")
