from django import forms
from .models import catagories

class addcatagories(forms.ModelForm):
    class Meta:
        model = catagories
        fields = '__all__'