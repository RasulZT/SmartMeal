from django.urls import path

from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserProfileAPIView.as_view(), name='profile'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    #user
    path("me/", UserProfileAPIView.as_view(), name="user-profile"),
    path("saved-recipes/", SavedRecipesAPIView.as_view(), name="saved-recipes")
]
