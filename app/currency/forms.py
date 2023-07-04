from django import forms
from currency.models import Contacts, Rates, Source


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = (
            'email_from',
            'subject',
            'message'
        )
        labels = {
            'email_from': 'Email',
            'subject': 'Subject',
            'message': 'Message'
        }
        widgets = {
            'email_from': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Enter the subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message'}),
        }

class RatesForm(forms.ModelForm):
    class Meta:
        model = Rates
        fields = (
            'currency',
            'buy',
            'sell',
            'source'
        )
        labels = {
            'currency': 'Currency',
            'buy': 'Buy',
            'sell': 'Sell',
            'source': 'Source',
        }
        widgets = {
            'currency': forms.TextInput(attrs={'placeholder': 'Enter currency shortcut (usd, uah, etc.)'}),
        
            'source': forms.TextInput(attrs={'placeholder': 'Enter cuurency rate source'}),
        }