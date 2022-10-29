
from tkinter.tix import Form
from django import forms

class FormularioEmpleados(forms.Form):
    CARGO=(
        (1, 'Cheff'),
        (2, 'Administrador'),
        (3, 'Mesero'),
        (4, 'Ayudante')
    )
    nombre=forms.CharField(
        required=True,
        max_length=5,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    apellidos=forms.CharField(
        required=False,
        max_length=20,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})

    )
    foto=forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})

    )
    cargo=forms.ChoiceField(
        required=True, 
        widget=forms.Select(attrs={'class':'form-select mb-3'}),
        choices=CARGO
    )
    salario=forms.CharField(
        required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})

    )
    contacto=forms.CharField(
        required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})
    )