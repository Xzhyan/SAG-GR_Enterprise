from django.urls import path

# views
from .views import admin_views

urlpatterns = [
    path('', admin_views.administration, name='administration'),
]
