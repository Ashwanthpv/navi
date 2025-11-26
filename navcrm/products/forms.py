from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Product Name', 'required': True}),
            'price': forms.NumberInput(attrs={'placeholder': 'Price', 'step': '0.01', 'required': True}),
            'description': forms.Textarea(attrs={'placeholder': 'Description', 'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = self.fields[field].label.replace('_', ' ').title()

