from django import forms
from .models import Dog

class DogCreateForm(forms.ModelForm):
    images = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Dog
        fields = ['name', 'breed', 'age', 'description','images']