from django import forms
from . import models


class CreateItem(forms.ModelForm):
    class Meta:
        model = models.RentalItem
        fields = ['item_name', 'price', 'image']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Search items...'}))