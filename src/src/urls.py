"""src URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.apps import apps


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', include(apps.get_app_config('oscar').urls[0])),
]
