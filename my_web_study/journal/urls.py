from django.urls import path
from .views import jindex


app_name = 'main'

urlpatterns = [
    path('journal/', jindex),
]