from django.urls import path

# views
from .views import auth_view

urlpatterns = [
    path('', auth_view.user_login, name='user-login')
]
