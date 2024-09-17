from django import forms
from . import models

import accounts.models

class CreateItem(forms.ModelForm):
    class Meta:
        model = models.RentalItem
        fields = ['item_name', 'price']

