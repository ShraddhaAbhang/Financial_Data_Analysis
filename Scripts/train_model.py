# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_absolute_error, mean_squared_error
# import os

# # Define file path
# INPUT_FILE = "../Data/Extracted/cleaned_financial_data.csv"

# # Load the data
# df = pd.read_csv(INPUT_FILE)

# # Selecting relevant financial metrics for prediction
# features = ["Year", "Total Revenue", "Net Income", "Total Assets", "Total Liabilities"]
# target = "Cash Flow from Operating Activities"

# # Drop rows with missing values
# df = df.dropna(subset=features + [target])

# # Split data into train and test sets
# X = df[features]
# y = df[target]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train a RandomForestRegressor model
# model = RandomForestRegressor(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)

# # Make predictions
# y_pred = model.predict(X_test)

# # Evaluate the model
# mae = mean_absolute_error(y_test, y_pred)
# mse = mean_squared_error(y_test, y_pred)
# rmse = np.sqrt(mse)

# print("📊 Model Evaluation Metrics:")
# print(f"🔹 Mean Absolute Error (MAE): {mae:.2f}")
# print(f"🔹 Mean Squared Error (MSE): {mse:.2f}")
# print(f"🔹 Root Mean Squared Error (RMSE): {rmse:.2f}")

# # Save the model
# import joblib
# os.makedirs("../Models", exist_ok=True)
# model_path = "../Models/financial_prediction_model.pkl"
# joblib.dump(model, model_path)

# print(f"✅ Model saved at {model_path}")

# # Plot actual vs predicted
# plt.figure(figsize=(10, 5))
# plt.scatter(y_test, y_pred, alpha=0.7)
# plt.xlabel("Actual Cash Flow")
# plt.ylabel("Predicted Cash Flow")
# plt.title("Actual vs Predicted Cash Flow")
# plt.grid()
# plt.savefig("../Reports/actual_vs_predicted_cash_flow.png")
# plt.show()

import pandas as pd
import os

# Define file path
INPUT_FILE = "../Data/Extracted/cleaned_financial_data.csv"

# Check if the file exists
if not os.path.exists(INPUT_FILE):
    raise FileNotFoundError(f"❌ Error: File not found -> {INPUT_FILE}")

# Load the CSV file
df = pd.read_csv(INPUT_FILE)

# Check if DataFrame is empty
if df.empty:
    raise ValueError("❌ Error: The CSV file is empty. Ensure data has been properly extracted and cleaned.")

print(f"✅ CSV file loaded successfully! Shape: {df.shape}")
print(df.head())  # Display first few rows

