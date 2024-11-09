from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings

app_name = 'items'

urlpatterns = [
    path('', views.items, name='items-list'),
    path('create-listing', views.create_listing, name='create-listing'),
    path('<int:item_id>', views.item_detail, name='item-detail'),
    path('checkout-success', views.checkout_success, name='checkout-success'),
    path('checkout-failed', views.checkout_failed, name='checkout-failed')
]