"""src URL Configuration
"""
from django.urls import path

from .views import IndexView, AboutUsView

urlpatterns = [
    path('', IndexView.as_view(), name='ui_index'),
    path('about-us', AboutUsView.as_view())
]
