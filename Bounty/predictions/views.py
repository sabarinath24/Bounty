from django.shortcuts import render, redirect
from .forms import PredictionForm
from django.contrib.auth.decorators import login_required
from .models import Prediction
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

# Dummy function to simulate predictive analytics
def predict_materials(data):
    model = LinearRegression()
    model.fit(data[['feature1', 'feature2']], data['target'])
    predictions = model.predict(data[['feature1', 'feature2']])
    return predictions
@login_required
def create_prediction(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            prediction = form.save(commit=False)
            prediction.predictor = request.user
            # Example of predicting data
            # Assuming you have a DataFrame 'data' with the required columns
            data = pd.DataFrame({
                'feature1': [1, 2, 3],
                'feature2': [4, 5, 6],
                'target': [7, 8, 9]
            })
            predicted_values = predict_materials(data)
            prediction.prediction_text = str(predicted_values)
            prediction.save()
            return redirect('prediction_list')
    else:
        form = PredictionForm()
    return render(request, 'predictions/create_prediction.html', {'form': form})

def prediction_list(request):
    predictions = Prediction.objects.filter(predictor=request.user)
    return render(request, 'predictions/prediction_list.html', {'predictions': predictions})
