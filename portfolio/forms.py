from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['full_name', 'email', 'address', 'number', 'skill', 'image']
