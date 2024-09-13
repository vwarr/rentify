from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('', views.items, name='items-list'),
    path('create-listing', views.create_listing, name='create-listing'),
]