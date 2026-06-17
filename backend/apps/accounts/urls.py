from django.urls import path

from .views import (
    UserLoginView,
    UserProfileUpdateView,
    UserProfileView,
    UserRegisterView,
    user_logout_view,
)

app_name = "accounts"

urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", user_logout_view, name="logout"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("profile/edit/", UserProfileUpdateView.as_view(), name="profile_edit"),
]
