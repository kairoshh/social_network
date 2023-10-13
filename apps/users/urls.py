from apps.users.views import UserRegistrationView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
   
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
urlpatterns = [
    path('registration/', UserRegistrationView.as_view()),
    path('token/', TokenObtainPairView.as_view())
]

urlpatterns += router.urls
