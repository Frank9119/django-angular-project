from django.contrib import admin
from django.urls import path, include
from accounts.views import *

## rest_framework_simplejwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

## rest framework
from rest_framework.routers import DefaultRouter

from jobs.views import JobViewSet


router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='jobs')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts Endpoints
    path('api/register/', RegisterView.as_view()),
    path('api/login/', TokenObtainPairView.as_view()),
    path('api/refresh/', TokenRefreshView.as_view()),
    path('api/change-password/', ChangePasswordView.as_view()),
    path('api/reset-password/', ResetPasswordView.as_view()),
    path('api/logout/', LogoutView.as_view()),

    path('api/', include(router.urls)),
]
