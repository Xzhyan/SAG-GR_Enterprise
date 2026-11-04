from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages


User = get_user_model() # modelo do usuário

# forms
from user.forms import LoginForm


def user_login(request: HttpRequest) -> HttpResponse:
    """Tela de login do usuário"""

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(request, "Acesso autorizado!")
            return redirect('user-login')

        else:
            messages.error(request, "Acesso negado!")

    else:
        form = LoginForm()

    context = {
        'form': form,
    }

    return render(request, 'user/login.html', context)


def user_logout(request: HttpRequest) -> HttpResponse:
    """Faz o logout do usuário logado"""

    logout(request)

    messages.success(request, "Sessão finalizada!")
    return redirect('user-login')
