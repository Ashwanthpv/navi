from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'client', 'due_date', 'priority']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Task Title', 'required': True}),
            'client': forms.Select(attrs={'required': True}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'required': True}),
            'priority': forms.Select(attrs={'required': True}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].label = self.fields[field].label.replace('_', ' ').title()

