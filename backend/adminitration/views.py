from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def administration(request: HttpRequest) -> HttpResponse:
    """Tela de administração"""

    context = {

    }

    return render(request, 'admin/administration.html', context)
