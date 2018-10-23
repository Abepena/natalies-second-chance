from django import forms
from django.core import validators
from django.utils.safestring import mark_safe
from django.forms.widgets import ClearableFileInput
from .models import Dog

class ImageClearableFileInput(ClearableFileInput):
    #remove the label 'Change' from the image button as it will be hidden with CSS
    input_text = ''

class DogCreateForm(forms.ModelForm):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(attrs={"rows":7}))
    image = forms.ImageField(
        label=mark_safe('<i class="fas fa-download"></i> Choose Image...'),
        widget=ImageClearableFileInput,
        required=False
    )

    class Meta:
        model = Dog
        fields = ['name', 'breed', 'age', 'size', 'sex', 'description', 'image' ]