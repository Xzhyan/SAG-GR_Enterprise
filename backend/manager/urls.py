from django.urls import path

# views
from .views import department_views

urlpatterns = [
    path('', department_views.department, name='department'),
]
