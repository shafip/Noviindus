from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms




class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','image', 'brand', 'price']

class UpdateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','image', 'brand', 'price']
