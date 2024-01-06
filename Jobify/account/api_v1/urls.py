from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/',RegisterUserView.as_view(),name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/',LogoutUserView.as_view(),name='logout'),
    path('profile-list/<int:id>/',ProfileListView.as_view(),name='profile-list')

]