from django import forms
from .models import Doctor

class DoctorCreationForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('name', 'email', 'phone','department', 'description', 'photo')