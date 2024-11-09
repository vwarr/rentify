import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from . import forms
from .models import RentalItem, UserPayment
import stripe


# Create your views here.

def items(request):
    rental_items = RentalItem.objects.filter(available=True)
    return render(request, "items.html", {'rental_items': rental_items})


def item_detail(request, item_id):
    item = get_object_or_404(RentalItem, id=item_id)
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    if request.method == 'POST':
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.item_name,
                        },
                        'unit_amount': int(item.price * 100),
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=reverse_lazy('items:checkout-success'),
            cancel_url=reverse_lazy('items:checkout-failed')
        )
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


def checkout_success(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    checkout_session_id = request.GET.get('checkout_session_id', None)
    session = stripe.checkout.Session.retrieve(checkout_session_id)
    customer = stripe.Customer.retrieve(session.customer)
    user_id = request.user.id
    payment = UserPayment.objects.get(user=user_id)
    payment.stripe_checkout_id = checkout_session_id
    payment.save()
    return render(request, 'checkout-success.html', {'customer': customer})


def checkout_failed(request):
    return render(request, 'checkout-failed.html')
