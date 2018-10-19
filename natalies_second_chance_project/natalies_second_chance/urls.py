"""natalies_second_chance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.urls import path, include
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('contact/', views.ContactPageView.as_view(template_name='contact.html'), name='contact'),
    path('dogs/', include('dogs.urls')),
    path('events/', views.TemplateView.as_view(template_name='events.html'), name='events'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('test_login/', views.test_user_login, name='test_login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
