from django import forms
from .models import Dog

class DogCreateForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'breed', 'age', 'description',]