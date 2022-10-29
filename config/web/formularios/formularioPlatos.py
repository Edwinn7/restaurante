
from tkinter.tix import Form
from django import forms

class FormularioPlatos(forms.Form):
    PLATOS=(
        (1, 'Entradas'),
        (2, 'Plato fuerte'),
        (3, 'Postre')
    )
    nombre=forms.CharField(
        required=True,
        max_length=5,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})
    )
    descripcion=forms.CharField(
        required=False,
        max_length=20,
        widget=forms.Textarea(attrs={'class':'form-control mb-3'})

    )
    foto=forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class':'form-control mb-3'})

    )
    precio=forms.CharField(
        required=True,
        max_length=20,
        widget=forms.NumberInput(attrs={'class':'form-control mb-3'})

    )
    tipo=forms.ChoiceField(
        required=True, 
        widget=forms.Select(attrs={'class':'form-select mb-3'}),
        choices=PLATOS
    )