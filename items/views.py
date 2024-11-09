import os

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from . import forms
from .models import Item, Category


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

def item_list(request):
    query = request.GET.get('query', '')  # Get the search query from the URL
    rental_items = Item.objects.all()  # Get all items by default
    category_id = request.GET.get('category', None)  # Make sure category_id is set to None if not provided
    categories = Category.objects.all()

    if query:
        # Filter items by item_name using case-insensitive search
        rental_items = rental_items.filter(item_name__icontains=query)
    if category_id:
        rental_items = rental_items.filter(category_id=category_id)

    context = {
        'rental_items': rental_items,
        'categories': categories,
        'query': query,  # Pass the query back to the template for displaying in the search bar
        'selected_category': int(category_id) if category_id else None,
    }
    return render(request, 'items.html', context)
