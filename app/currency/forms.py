from django import forms
from currency.models import Contacts


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

