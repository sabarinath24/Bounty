from django.db import models
from deeds.models import Deed
from users.models import User

class Prediction(models.Model):
    deed = models.ForeignKey(Deed, on_delete=models.CASCADE)
    predictor = models.ForeignKey(User, on_delete=models.CASCADE)
    prediction_text = models.TextField()
    outcome = models.CharField(max_length=50, choices=[('success', 'Success'), ('failure', 'Failure')])
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)
