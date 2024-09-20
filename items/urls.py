from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings

app_name = 'items'

urlpatterns = [
    path('', views.items, name='items-list'),
    path('create-listing', views.create_listing, name='create-listing'),
]