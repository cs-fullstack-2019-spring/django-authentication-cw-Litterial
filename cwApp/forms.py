from django import forms
from .models import FoodFitness

class FoodFitnessForm(forms.ModelForm):
    class Meta:
        model=FoodFitness
        exclude=['userTableForeignKey']
