from django.urls import path
from . views import *

urlpatterns = [
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
    path('token_send', token_send, name='token_send'),
    path('success', success, name='success')
]