from tkinter.tix import Form
from django import forms


class FormularioReservas(forms.Form):
    nombre = forms.CharField(
        required=True,
        label='Nombre',
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    email = forms.CharField(
        required=True,
        label='Email',
        widget=forms.TextInput(attrs={'class': 'form-control mb-3'})
    )
    fecha  = forms.CharField(
        required=True,
        label='Fecha de reserva',
        widget=forms.DateTimeInput(attrs={'class': 'form-control mb-3'})
    )
    hora = forms.CharField(
        required=True,
        label='Email',
        widget=forms.TimeInput(attrs={'class': 'form-control mb-3'})
    )
    cantidad_personas = forms.CharField(
        required=True,
        label='Cantidad de personas',
        widget=forms.NumberInput(attrs={'class': 'form-control mb-3'})
    )
def clean_cantidad_personas(self):
        cantidad = self.cleaned_data.get('cantidad_personas')
        if cantidad <= 0:
            raise forms.ValidationError('La cantidad de personas debe ser mayor a cero.')
        return cantidad