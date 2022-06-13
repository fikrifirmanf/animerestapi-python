from django.urls import path

from scraper.views import get_all, get_by_slug, get_stream_by_slug


app_name = 'scraper'

urlpatterns = [
    path('anime', get_all),
    path('anime/<str:slug>/detail', get_by_slug),
    path('anime/<str:slug>/stream', get_stream_by_slug)
]