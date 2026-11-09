from django.urls import path

# views
from .views import admin_views, user_views

urlpatterns = [
    # Páginas principais (Organização)
    path('', admin_views.administration, name='administration'),
    path('organization/<int:id>/', admin_views.update_org, name='update-org'),

    # Usuários
    path('users/', user_views.manage_users, name='manage-users')
]
