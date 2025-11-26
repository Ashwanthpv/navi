from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    order_status = forms.ChoiceField(
        choices=Client.ORDER_STATUS_CHOICES,
        widget=forms.RadioSelect(),
        required=False
    )
    
    class Meta:
        model = Client
        fields = ['full_name', 'email', 'phone', 'company', 'product', 'product_description', 'order_status']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'required': True}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number', 'required': True}),
            'company': forms.TextInput(attrs={'placeholder': 'Company Name'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'product_description': forms.Textarea(attrs={'placeholder': 'Product Description', 'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field != 'order_status':
                self.fields[field].label = self.fields[field].label.replace('_', ' ').title()

