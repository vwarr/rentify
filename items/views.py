import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from . import forms
from .models import RentalItem


# Create your views here.

def items(request):
    rental_items = RentalItem.objects.filter(available=True)
    return render(request, "items.html", {'rental_items': rental_items})


def item_detail(request, item_id):
    item = get_object_or_404(RentalItem, id=item_id)
    return render(request, 'item-detail.html', {'item': item})


@login_required(login_url=reverse_lazy('accounts:login'))
def create_listing(request):
    if request.method == 'POST':
        form = forms.CreateItem(request.POST, request.FILES)
        if form.is_valid():
            item = RentalItem.objects.create(
                item_name=form.cleaned_data['item_name'],
                price=form.cleaned_data['price'],
                image=form.files['image'],
                renter_first_name=request.user.first_name,
                renter_last_name=request.user.last_name
            )
            item.save()
            return redirect(reverse('items:items-list'))
    else:
        form = forms.CreateItem()
    return render(request, 'create-listing.html', {'form': form})
