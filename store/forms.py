from django import forms
from store.models import  Product

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'image','instock', 'description', 'category')

class SearchForm(forms.Form):
    find = forms.CharField(required=False)
