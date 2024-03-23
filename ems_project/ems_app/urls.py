from django.urls import path
from .views import details, find_events

urlpatterns = [
    path('events/', details),
    path('events/find/',find_events),
]