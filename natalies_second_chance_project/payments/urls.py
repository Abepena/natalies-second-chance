from django.urls import path
from .views import HomePageView, ChargeView

urlpatterns = [
    path('', HomePageView.as_view(), name="home" ),
    path('charge/', ChargeView.as_view(), name="charge")
]