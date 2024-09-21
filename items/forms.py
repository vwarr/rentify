from django import forms
from . import models


class CreateItem(forms.ModelForm):
    class Meta:
        model = models.RentalItem
        fields = ['item_name', 'price', 'image']

