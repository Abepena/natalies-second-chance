from django import forms
from django.core import validators
from django.utils.safestring import mark_safe
from .models import Dog


class DogCreateForm(forms.ModelForm):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":5}))
    image = forms.ImageField(
        label=mark_safe('<i class="fas fa-download"></i> Choose Image...'),
        widget=forms.FileInput(
            attrs={'class': 'inputfile'}
        ),
    )

    class Meta:
        model = Dog
        fields = ['name', 'breed', 'age', 'description','image']