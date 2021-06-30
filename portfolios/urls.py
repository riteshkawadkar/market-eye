from django.urls import path
from . views import *

urlpatterns = [
    path('portfolio', portfolio, name='portfolio'),
]