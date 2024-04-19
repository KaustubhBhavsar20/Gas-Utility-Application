from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['type', 'description']  # Include the fields from your ServiceRequest model here

    # Optionally, you can add custom validation or widgets for your fields here
    # For example, to add a Textarea widget for the description field:
    # widgets = {
    #     'description': forms.Textarea(attrs={'rows': 5}),
    # }
