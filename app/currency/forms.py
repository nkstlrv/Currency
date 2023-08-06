from django import forms
from .models import ContactUs, Rate, Source


class ContactsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ("email_from", "subject", "message")
        labels = {"email_from": "Email", "subject": "Subject", "message": "Message"}
        widgets = {
            "email_from": forms.EmailInput(attrs={"placeholder": "Enter your email"}),
            "subject": forms.TextInput(attrs={"placeholder": "Enter the subject"}),
            "message": forms.Textarea(attrs={"placeholder": "Enter your message"}),
        }


class RatesForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ("currency", "buy", "sell", "source")
        labels = {
            "currency": "Currency",
            "buy": "Buy",
            "sell": "Sell",
            "source": "Source",
        }


class SourcesForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = ("name", "url", "logo")
        labels = {"name": "Source Name", "url": "Source URL"}
        widgets = {
            "email_from": forms.TextInput(attrs={"placeholder": "Enter source name"}),
            "subject": forms.TextInput(attrs={"placeholder": "Enter source URL"}),
        }
