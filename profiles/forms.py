from django import forms
from .models import profile

class profiles_form(forms.ModelForm):
    class Meta:
        model = profile
        fields = '__all__'