from django.urls import path
from django.views.generic import TemplateView # Renders a given template, with the context containing parameters captured in the URL.


app_name = 'blog'

urlpatterns = [
    path("", TemplateView.as_view(template_name='blog/index.html')),
    
]
