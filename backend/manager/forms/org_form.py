from django import forms
from ..models import Organization


class OrganizationForm(forms.ModelForm):
    """From do modelo Organization"""

    class Meta:
        model = Organization
        fields = [
            'name',
            'acronym',
            'cnpj',
            'email',
            'contact',
            'address',
            'city',
            'state'
        ]

        labels = {
            'name': "Nome",
            'acronym': "Sigla",
            'cnpj': "CNPJ",
            'email': "E-mail",
            'contact': "Contato",
            'address': "Endereço",
            'city': "Cidade",
            'state': "Estado"
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': "w-full bg-zinc-900 hover:bg-zinc-800 transition border border-zinc-800 p-2 rounded-md shadow-md outline-none",
                    'placeholder': "Nome da organização..."
                }
            ),

            'acronym': forms.TextInput(
                attrs={
                    'class': "w-full bg-zinc-900 hover:bg-zinc-800 transition border border-zinc-800 p-2 rounded-md shadow-md outline-none",
                    'placeholder': "Sigla da organização..."
                }
            ),

            'cnpj': forms.TextInput(
                attrs={
                    'class': "w-full bg-zinc-900 hover:bg-zinc-800 transition border border-zinc-800 p-2 rounded-md shadow-md outline-none",
                    'placeholder': "CNPJ da organização"
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': "w-full bg-zinc-900 hover:bg-zinc-800 transition border border-zinc-800 p-2 rounded-md shadow-md outline-none",
                    'placeholder': "E-mail da organização"
                }
            ),

            'contact': forms.TextInput(
                attrs={
                    'class': "w-full bg-zinc-900 hover:bg-zinc-800 transition border border-zinc-800 p-2 rounded-md shadow-md outline-none",
                    'placeholder': "Número de contato da organização..."
                }
            ),

            'address': forms.TextInput(
                attrs={
                    'class': "w-full bg-zinc-900 hover:bg-zinc-800 transition border border-zinc-800 p-2 rounded-md shadow-md outline-none",
                }
            ),

            'city': forms.TextInput(
                attrs={
                    'class': "w-full bg-zinc-900 hover:bg-zinc-800 transition border border-zinc-800 p-2 rounded-md shadow-md outline-none",
                    'placeholder': "Nome da cidade onde se localiza..."
                }
            ),

            'state': forms.Select(
                attrs={
                    'class': "w-full bg-zinc-900 hover:bg-zinc-800 transition border border-zinc-800 p-2 rounded-md shadow-md outline-none",
                }
            ),
        }
