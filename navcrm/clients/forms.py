from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['full_name', 'email', 'phone', 'company']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'required': True}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number', 'required': True}),
            'company': forms.TextInput(attrs={'placeholder': 'Company Name'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = self.fields[field].label.replace('_', ' ').title()

