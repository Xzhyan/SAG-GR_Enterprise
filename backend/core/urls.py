from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Browser Reload
    path('__reload__/', include('django_browser_reload.urls')),

    # Admin
    path('admin/', admin.site.urls),

    # Usuário, autenticação
    path('', include('user.urls')),

    # Departamentos
    path('department', include('manager.urls')),
]
