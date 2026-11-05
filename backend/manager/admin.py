from django.contrib import admin

from .models import (
    Organization,
    Department,
    MemberSkill,
    Member,
    Process,
    ProcessStep
)

models = [
    Organization,
    Department,
    MemberSkill,
    Member,
    Process,
    ProcessStep
]

for model in models:
    admin.site.register(model)
