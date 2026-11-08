from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.core.exceptions import PermissionDenied
from django.contrib.auth import login, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.models import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
import json

# models
from manager.models import AuditLog, Organization

# forms
from manager.forms.org_form import OrganizationForm


@login_required
def administration(request: HttpRequest) -> HttpResponse:
    """Tela de administração do sistema"""

    # Apenas usuários com 'staff' podem acessar o sistema
    if not request.user.is_staff:
        raise PermissionDenied()

    org = Organization.objects.first()

    if request.method == 'POST':
        form = OrganizationForm(request.POST)

        if form.is_valid():
            org = form.save()

            # Organiza os campos do modelo para salvar no Auditlog
            changes = model_to_dict(org)
            changes = json.loads(json.dumps(changes, cls=DjangoJSONEncoder))

            AuditLog.objects.create(
                modified_by=request.user,
                action=AuditLog.Action.CREATE,
                model_name=Organization.__name__,
                object_id=org.id,
                changes=changes
            )

            messages.success(request, "Organização adicionada com sucesso!")
            messages.info(request, "Os trabalhos já podem começar...")

            return redirect('administration')

        else:
            messages.error(request, "Erro ao adicionar a organização!")

    else:
        form = OrganizationForm()

    context = {
        'org': org,
        'form': form,

        # controle de páginas do admin
        'org_page': True,
    }

    return render(request, 'administration/admin.html', context)
