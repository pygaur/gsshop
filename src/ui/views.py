"""
"""
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "ui/index.html"


class AboutUsView(TemplateView):
    template_name = "ui/about-us.html"
