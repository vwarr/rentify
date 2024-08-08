from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

from .models import RentalItem


# Create your views here.

def items(request):
    rental_items = RentalItem.objects.filter(available=True)
    return render(request, "items.html", {'rental_items': rental_items})


@login_required(login_url=reverse_lazy('accounts:login'))
def create_listing(request):
    return render(request, 'create-listing.html')
