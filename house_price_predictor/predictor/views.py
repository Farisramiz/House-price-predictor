from django.shortcuts import render
from .Forms import HouseForm
from .models import Prediction
import pickle, os
import numpy as np
from django.http import JsonResponse

model_path = os.path.join(os.path.dirname(__file__), 'predictor_model', 'model.pkl')

model = None
if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print("✅ Model loaded successfully")
else:
    print(f"❌ Model file not found at: {model_path}")

def predict_price(request):
    predicted_price = None
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            features = np.array([[data['bedrooms'], data['bathrooms'], data['sqft_living'], data['floors']]])
            predicted_price = model.predict(features)[0]
            Prediction.objects.create(**data, predicted_price=predicted_price)
    else:
        form = HouseForm()
    return render(request, 'predictor/predict.html', {'form': form, 'predicted_price': predicted_price})
