from django.contrib import admin

from .models import (
    Organization,
    Department,
    MemberSkill,
    Member,
    Process,
    ProcessStep,
    AuditLog
)

models = [
    Organization,
    Department,
    MemberSkill,
    Member,
    Process,
    ProcessStep,
    AuditLog
]

for model in models:
    admin.site.register(model)
