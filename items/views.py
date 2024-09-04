from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from . import forms
from .models import RentalItem


# Create your views here.

def items(request):
    rental_items = RentalItem.objects.filter(available=True)
    return render(request, "items.html", {'rental_items': rental_items})


@login_required(login_url=reverse_lazy('accounts:login'))
def create_listing(request):
    if request.method == 'POST':
        form = forms.CreateItem(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('items:items-list'))
    else:
        form = forms.CreateItem()
    return render(request, 'create-listing.html', {'form': form})
