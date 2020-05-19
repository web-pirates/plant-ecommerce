from django import forms

class Product(forms.Form):
    pname = forms.CharField(label='Product name', max_length=100)
    price = forms.IntegerField(label='Product price')