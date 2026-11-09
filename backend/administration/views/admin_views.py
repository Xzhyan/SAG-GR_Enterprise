# Shortcuts
from django.shortcuts import render, redirect, get_object_or_404

# Http
from django.http import HttpRequest, HttpResponse

# Contrib
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Core
from django.core.exceptions import PermissionDenied
from django.core.serializers.json import DjangoJSONEncoder

# Outros
import json

# models
from django.forms.models import model_to_dict
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

    if org == None:
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

    else:
        form = False

    context = {
        'org': org,
        'form': form,

        # controle de páginas do admin
        'manage_org': True,
    }

    return render(request, 'administration/admin.html', context)


@login_required
def update_org(request: HttpRequest, id: int) -> HttpResponse:
    """Tela de atualizar organização"""

    # Apenas usuários com 'staff' podem acessar o sistema
    if not request.user.is_staff:
        raise PermissionDenied()

    org = get_object_or_404(Organization, pk=id)

    if request.method == 'POST':
        form = OrganizationForm(request.POST, instance=org)

        if form.is_valid():
            org = form.save()

            # Organiza os campos do modelo para salvar no Auditlog
            changes = model_to_dict(org)
            changes = json.loads(json.dumps(changes, cls=DjangoJSONEncoder))

            AuditLog.objects.create(
                modified_by=request.user,
                action=AuditLog.Action.UPDATE,
                model_name=Organization.__name__,
                object_id=org.id,
                changes=changes
            )

            messages.success(request, "Organização atualizada com sucesso!")

            return redirect('administration')

        else:
            messages.error(request, "Erro ao atualizar a organização!")

    else:
        form = OrganizationForm(instance=org)

    context = {
        'org': org,
        'form': form,

        # controle do modo editar
        'editing': True,

        # controle de páginas do admin
        'manage_org': True,
    }

    return render(request, 'administration/admin.html', context)

