from django import forms
from .models import User
from django.contrib.auth import get_user_model
from currency.tasks import send_signup_verify_email
from django.conf import settings
from django.urls import reverse

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
# from django.urls import reverse_lazy


class PasswordResetForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        label="Enter new password",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm new password",
    )

    def clean_email(self):
        email = self.cleaned_data.get("email").lower()
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with this email does not exist.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

    def save(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password1")
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()


class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "password1",
            "password2",
        )

    def clean(self):
        clened_data = super().clean()

        if not self.errors:
            if clened_data["password1"] != clened_data["password2"]:
                raise forms.ValidationError("Passwords do not match")

        return clened_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        instance.set_password(self.cleaned_data["password1"])
        instance.is_active = False

        instance.save()
        self._send_mail()
        return instance

    def _send_mail(self):
        activate_path = reverse("activate", args=(self.instance.username,))
        subject = "Confirm Registration"
        body = f"""
            {settings.HTTP_PROTOCOL}://{settings.DOMAIN}{activate_path}
        """

        send_signup_verify_email.delay(
            subject, body, settings.DEFAULT_FROM_EMAIL, self.instance.email
        )
