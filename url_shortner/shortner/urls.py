"""
Logic for handling urls
"""
from django.urls import path
from shortner.views import GetShortenUrl, CreateShortUrl


urlpatterns = [
    path('get/<str:referenceId>', GetShortenUrl.as_view()),
    path('create', CreateShortUrl.as_view())
 
]