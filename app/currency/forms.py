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
