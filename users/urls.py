from django.urls import path
from .views import UserView, UserLoginView, UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/login/', UserLoginView.as_view()),
    path('users/login/refresh', TokenRefreshView.as_view()),
    path('users/<int:user_id>/', UserDetailView.as_view())
]
