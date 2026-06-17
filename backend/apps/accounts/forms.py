from django import forms

from .models import UserProfile


class UserRegistrationForm(forms.ModelForm):
    """
    Form used to register a new Troc user.

    Phone number is required.
    Email is optional.
    """

    password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8,
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        min_length=8,
    )

    class Meta:
        model = UserProfile
        fields = [
            "phone_number",
            "email",
            "first_name",
            "last_name",
            "country",
            "region",
            "city",
            "local_area",
            "password",
            "confirm_password",
        ]

    def clean(self):
        """
        Validate that password and confirm_password are identical.
        """

        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
