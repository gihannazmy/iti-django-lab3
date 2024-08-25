from django import forms
from .models import Trainee  # Import the Trainee model

class TraineeForm(forms.ModelForm):
    class Meta:
        model = Trainee
        fields = ['name', 'email']