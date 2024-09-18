from django.conf.urls.static import static
from django.urls import path
from . import views
from django.conf import settings

app_name = 'items'

urlpatterns = [
    path('', views.items, name='items-list'),
    path('create-listing', views.create_listing, name='create-listing'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)