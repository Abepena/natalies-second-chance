from django.urls import path
from .views import DogCreateView

app_name = 'dogs'

urlpatterns = [
    path('create/', DogCreateView.as_view(), name='create' ),
    
]