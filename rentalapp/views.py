from django.http import HttpResponse
from django.shortcuts import render

from .models import RentalItem


# Create your views here.

def items(request):
    rental_items = RentalItem.objects.filter(available=True)
    return render(request, "items.html", {'rental_items': rental_items})
