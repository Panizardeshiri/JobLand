from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/',RegisterUserView.as_view(),name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/',LogoutUserView.as_view(),name='logout'),
    path('profile-list/<int:id>/',ProfileListView.as_view(),name='profile-list'),
    path('add-address/',AddAddressView.as_view(),name='add-adderess'),
    path('edit-profile/',EditProfileView.as_view(),name='edit-profile'),
    path('edit-address/<int:id>',EditAdressView.as_view(),name='edit-address'),
    path('add-skill/',AddSkillView.as_view(),name='add-skill'),

]