from django import forms
from .models import Subscribers

class SubscribersForm(forms.ModelForm):
    class Meta():
        model = Subscribers
        fields = ('email','name')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'signup-input', 'name': 'email'}),
            'name': forms.TextInput(attrs={'class': 'signup-input', 'name':'name'}),
        }
