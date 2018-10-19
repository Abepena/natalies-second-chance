from django.urls import path
from . import views
from django.conf.urls.static import static #allows django to serve up media files
from django.conf import settings

app_name = 'dogs'

urlpatterns = [
    path('', views.DogListView.as_view(), name='list'),
    path('<int:pk>/', views.DogDetailView.as_view(), name='detail'),
    path('<int:pk>/delete', views.DogDeleteView.as_view(), name='delete'),
    path('create/', views.DogCreateView.as_view(), name='create' ),
    path('update/<int:pk>', views.DogUpdateView.as_view(), name='update'),
    
]


