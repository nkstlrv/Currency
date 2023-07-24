from django import forms
from django.contrib.auth.models import User

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
        email = self.cleaned_data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
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
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password1')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
