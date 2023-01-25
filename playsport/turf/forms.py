from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model=Productmodel
        fields=['id','photo','name','place','price']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'place':forms.TextInput(attrs={'class':'form-control'}),
            'PRICE':forms.TextInput(attrs={'class':'form-control'}),
        }
class Register(forms.ModelForm):
    class Meta:
        model=RegisterForm
        fields='__all__'