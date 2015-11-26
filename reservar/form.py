from django import forms
from .models import Habitacion
from .models import Reservar
class HabitacionForm(forms.ModelForm):

    class Meta:
        model = Habitacion
        fields = ('numero', 'capacidad','descripcion','imagen','precio','estado')

class ReservacionForm(forms.ModelForm):

    class Meta:
        model = Reservar
        fields = ('habitacion','descripcion','fechainicio','fechafinal')
    