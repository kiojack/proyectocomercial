from django.shortcuts import render
from .models import Habitacion
from django.utils import timezone
from .models import Reservar

# Create your views here.
def reservacion_list(request):
	reservar = Reservar.objects.filter(fechacreado__lte=timezone.now()).order_by('fechacreado')
	return render(request, 'reservar/reservacion_list.html', {'reservar': reservar})

def habitacion_list(request):
	habitacion = Habitacion.objects.all()
	return render(request, 'reservar/habitacion_list.html', {'habitacion': habitacion})
