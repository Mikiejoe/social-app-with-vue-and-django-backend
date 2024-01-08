from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.urls import path
from . import api

urlpatterns = [
    path('me/',api.me,name='me'),
    path('account/signup/',api.signup,name='signup'),
    path('account/login/',TokenObtainPairView.as_view(),name='token_obtain'),
    path('refresh/',TokenRefreshView.as_view(),name='token_refresh')
]
