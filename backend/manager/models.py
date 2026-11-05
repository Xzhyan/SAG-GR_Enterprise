from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Organization(models.Model):
    """Modelo de organização"""

    class State(models.TextChoices):
        AC = "AC", "Acre"
        AL = "AL", "Alagoas"
        AP = "AP", "Amapá"
        AM = "AM", "Amazonas"
        BA = "BA", "Bahia"
        CE = "CE", "Ceará"
        DF = "DF", "Distrito Federal"
        ES = "ES", "Espírito Santo"
        GO = "GO", "Goiás"
        MA = "MA", "Maranhão"
        MT = "MT", "Mato Grosso"
        MS = "MS", "Mato Grosso do Sul"
        MG = "MG", "Minas Gerais"
        PA = "PA", "Pará"
        PB = "PB", "Paraíba"
        PR = "PR", "Paraná"
        PE = "PE", "Pernambuco"
        PI = "PI", "Piauí"
        RJ = "RJ", "Rio de Janeiro"
        RN = "RN", "Rio Grande do Norte"
        RS = "RS", "Rio Grande do Sul"
        RO = "RO", "Rondônia"
        RR = "RR", "Roraima"
        SC = "SC", "Santa Catarina"
        SP = "SP", "São Paulo"
        SE = "SE", "Sergipe"
        TO = "TO", "Tocantins"

    name = models.CharField(
        max_length=150,
        unique=True
    )

    acronym = models.CharField(
        max_length=20,
        blank=True
    )

    cnpj = models.CharField(
        max_length=18,
        unique=True,
        blank=True
    )
    
    email = models.EmailField()

    contact = models.CharField(
        max_length=20
    )

    address = models.CharField(
        max_length=255
    )

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=2,
        choices=State.choices
    )

    def __str__(self) -> str:
        return self.name


class Department(models.Model):
    """Modelo do departamento"""

    manager = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name="department",
        null=True,
        blank=True
    )

    name = models.CharField(
        max_length=150,
        unique=True
    )

    description = models.TextField(
        max_length=255,
        blank=False
    )

    def __str__(self) -> str:
        return self.name


class MemberSkill(models.Model):
    """Modelo de habilidade, atribução especifica de um membro. ex: Programador"""

    name = models.CharField(
        max_length=200,
    )

    def __str__(self) -> str:
        return self.name


class Function(TimeStampedModel, models.Model):
    """Modelo das funções dos membros"""

    name = models.CharField(
        max_length=150,
        unique=True
    )

    description = models.TextField(
        max_length=255,
        blank=True
    )

    def __str__(self) -> str:
        return self.name


class Member(TimeStampedModel, models.Model):
    """Modelo dos membros"""

    name = models.CharField(
        max_length=150
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name='members'
    )

    role = models.ForeignKey(
        MemberRole,
        on_delete=models.PROTECT,
        related_name='members'
    )

    function = models.ForeignKey(
        Function,
        on_delete=models.PROTECT,
        related_name='members'
    )

    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class Assignment(models.Model):
    """Modelo de atribuições"""

    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name='assignment'
    )

    member = models.ForeignKey(
        Member,
        on_delete=models.SET_NULL,
        related_name='assignment',
        null=True,
        blank=True
    )

    name = models.CharField(max_length=150)

    description = models.TextField(max_length=500)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Process(TimeStampedModel, models.Model):
    """Modelo de processo de departamento"""

    name = models.CharField(max_length=150)
    
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="processes"
    )

    assignment = models.ForeignKey(
        Assignment,
        on_delete=models.PROTECT,
        related_name="processes"
    )

    description = models.TextField(max_length=500)

    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class ProcessStep(TimeStampedModel, models.Model):
    """Modelo de etapa de processo"""

    process = models.ForeignKey(
        Process,
        on_delete=models.CASCADE,
        related_name="steps"
    )

    order = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    description = models.TextField(max_length=500)

    department_involved = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name="process_steps",
        blank=True,
        null=True
    )

    external_department = models.CharField(
        max_length=255,
        blank=True
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['process', 'order'],
                name='unique_step_order_per_process'
            )
        ]

    def __str__(self) -> str:
        return str(self.order)


class AuditLog(models.Model):
    """Tabela de auditoria do sistema"""

    class Action(models.TextChoices):
        CREATE = "create", "Criação"
        UPDATE = "update", "Alteração"
        DELETE = "delete", "Exclusão"

    modified_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='audit_logs'
    )

    action = models.CharField(
        max_length=10,
        choices=Action.choices
    )

    model_name = models.CharField(
        max_length=100
    )

    object_id = models.PositiveIntegerField()

    changes = models.JSONField()

    modified_at = models.DateTimeField(auto_now_add=True)
