from django.urls import path, include
from .views.user_auth import *
app_name='account'

urlpatterns=[
    path('register/', UserRegistrationApiView.as_view(), name='register' )
]
