from django.urls import path
from .views import *

urlpatterns = [
    path('', meat_rice_view, name='meat-rice'),
    path('milk/', milk_view, name='milk'),
]