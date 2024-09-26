# forms.py
from django import forms
from .models import *
 
 
class PortfolioForm(forms.ModelForm):
 
    class Meta:
        model = Portfolio
        fields = ['name', 'detail','img']

        