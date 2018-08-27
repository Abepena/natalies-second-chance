from django.urls import path
from .views import DogCreateView, DogListView, DogUpdateView
from django.conf.urls.static import static #allows django to serve up media files
from django.conf import settings

app_name = 'dogs'

urlpatterns = [
    path('', DogListView.as_view(), name='list'),
    path('create/', DogCreateView.as_view(), name='create' ),
    path('update/', DogUpdateView.as_view(), name='update')
    
]

