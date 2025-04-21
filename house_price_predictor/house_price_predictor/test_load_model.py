import pickle
import os

model_path = os.path.join("predictor", "predictor_model", "model.pkl")

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print("🎉 Model loaded successfully!")
    print("📐 Model type:", type(model))
except Exception as e:
    print("❌ Failed to load model:", e)
