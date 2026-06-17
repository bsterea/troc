from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from .forms import UserRegistrationForm
from .models import UserProfile


class UserRegisterView(CreateView):
    """
    Handles new user registration.

    A new user registers with phone number, password and basic profile data.
    """

    model = UserProfile
    form_class = UserRegistrationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("accounts:profile")

    def form_valid(self, form):
        """
        Save the user and log them in immediately after registration.
        """

        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class UserLoginView(LoginView):
    """
    Handles user login.

    Authentication is based on phone number and password.
    """

    template_name = "accounts/login.html"


def user_logout_view(request):
    """
    Logs out the current user and redirects to the login page.
    """

    logout(request)
    return redirect("accounts:login")


class UserProfileView(LoginRequiredMixin, TemplateView):
    """
    Displays the logged-in user's profile.
    """

    template_name = "accounts/profile.html"


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    Allows the logged-in user to update their profile.
    """

    model = UserProfile
    fields = [
        "email",
        "first_name",
        "last_name",
        "country",
        "region",
        "city",
        "local_area",
        "preferred_language",
        "is_phone_public",
    ]
    template_name = "accounts/profile_edit.html"
    success_url = reverse_lazy("accounts:profile")

    def get_object(self, queryset=None):
        """
        Return the currently logged-in user.
        """

        return self.request.user


# END OF FILE
