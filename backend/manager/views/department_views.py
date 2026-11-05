from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages

User = get_user_model() # modelo do usuário

# models
from manager.models import (
    Department,
    Member,
    MemberSkill,
    Process,
    ProcessStep
)



@login_required
def department(request: HttpRequest) -> HttpResponse:
    """Tela de gerenciamento do departamento"""

    department = getattr(request.user, 'department', None)

    if not department:
        messages.info(request, "Você ainda não gerencia um departamento.")
        return redirect('user-login')

    members = Member.objects.filter(
        department=department,
        is_active=True
    )

    context = {
        'department': department,
        'members': members
    }

    return render(request, 'department/department.html', context)
