from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Browser Reload
    path('__reload__/', include('django_browser_reload.urls')),

    # Admin/Django
    path('admin/', admin.site.urls),

    # Admin
    path('saggr/admin/', include('administration.urls')),

    # Usuário, autenticação
    path('', include('user.urls')),

    # Departamentos
    path('department', include('manager.urls')),
]
