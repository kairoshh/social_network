from apps.posts.views import PostView
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
   
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', PostView)
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
]

urlpatterns += router.urls
