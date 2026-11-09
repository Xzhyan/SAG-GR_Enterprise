# Shortcuts
from django.shortcuts import render, redirect, get_object_or_404

# Http
from django.http import HttpRequest, HttpResponse

# Contrib
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Core
from django.core.exceptions import PermissionDenied
from django.core.serializers.json import DjangoJSONEncoder

# Outros
import json

# models
User = get_user_model()
from django.forms.models import model_to_dict
from manager.models import AuditLog, Organization

# forms
from manager.forms.org_form import OrganizationForm


@login_required
def manage_users(request: HttpRequest) -> HttpResponse:
    """Tela de gerenciamento de usuários"""

    users = User.objects.all()

    context = {
        'users': users,

        # controle de páginas do admin
        'manage_users': True,
    }

    return render(request, 'administration/admin.html', context)
