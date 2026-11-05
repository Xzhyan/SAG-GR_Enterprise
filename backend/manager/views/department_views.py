from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages


User = get_user_model() # modelo do usuário



def department(request: HttpRequest) -> HttpResponse:
    """Tela de gerenciamento do departamento"""

    context = {
    }

    return render(request, 'department/department.html', context)
