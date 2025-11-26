from django import forms
from .models import Deal

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['name', 'value', 'client', 'stage']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Deal Name', 'required': True}),
            'value': forms.NumberInput(attrs={'placeholder': 'Deal Value', 'step': '0.01', 'required': True}),
            'client': forms.TextInput(attrs={'placeholder': 'Client Name', 'required': True}),
            'stage': forms.Select(attrs={'required': True}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = self.fields[field].label.replace('_', ' ').title()
