from django import forms
from . import models


class CreateItem(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = ['item_name', 'price', 'image', 'category']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Search items...'}))