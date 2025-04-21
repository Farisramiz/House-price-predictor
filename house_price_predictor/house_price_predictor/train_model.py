import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
import os

print("🚀 Starting training script...")

# Load CSV
df = pd.read_csv("kc_house_data.csv")
print("✅ CSV loaded")

# Prepare data
X = df[['bedrooms', 'bathrooms', 'sqft_living', 'floors']]
y = df['price']
print("✅ Features selected")

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("✅ Data split")

# Train model
model = LinearRegression()
model.fit(X_train, y_train)
print("✅ Model trained")

# Save path
model_dir = os.path.join("predictor", "predictor_model")
os.makedirs(model_dir, exist_ok=True)
model_path = os.path.join(model_dir, "model.pkl")
abs_path = os.path.abspath(model_path)

# Save model
with open(model_path, "wb") as f:
    pickle.dump(model, f)

print(f"✅ Model saved at: {abs_path}")

# Check file size
size = os.path.getsize(model_path)
print(f"📏 File size: {size} bytes")
if size == 0:
    print("❌ ERROR: model.pkl is still empty")
else:
    print("🎉 SUCCESS: model.pkl saved and valid")
