from django.shortcuts import render, redirect
from .models import Habitacion
from django.utils import timezone
from .models import Reservar
from django.shortcuts import render, get_object_or_404
from .form import HabitacionForm, ReservacionForm

# Create your views here.
def reservacion_list(request):
	reservar = Reservar.objects.filter(fechacreado__lte=timezone.now()).order_by('fechacreado')
	return render(request, 'reservar/reservacion_list.html', {'reservar': reservar})

def habitacion_list(request):
	habitacion = Habitacion.objects.all()
	return render(request, 'reservar/habitacion_list.html', {'habitacion': habitacion})

def detalle_habitacion(request, pk):
    detallehab = get_object_or_404(Habitacion, pk=pk)
    return render(request, 'reservar/detalle_habitacion.html', {'post': detallehab})

def detalle_reservacion(request, pk):
    detallereservacion= get_object_or_404(Reservar, pk=pk)
    return render(request, 'reservar/detalle_reservacion.html', {'post': detallereservacion})

def nueva_hab(request):
    if request.method == "POST":
        form = HabitacionForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('reservar.views.detalle_habitacion', pk=post.pk)
    else:
        form = HabitacionForm()
    return render(request, 'reservar/editar_habitacion.html', {'form': form})

def editar_hab(request,pk):
	edihab = get_object_or_404(Habitacion, pk=pk)
	if request.method == "POST":
		form = HabitacionForm(request.POST, request.FILES, instance=edihab)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('reservar.views.detalle_habitacion', pk=post.pk)
	else:
		form = HabitacionForm(instance=edihab)
	return render(request, 'reservar/editar_habitacion.html', {'form': form})

def editar_reserva(request,pk):
    edireser = get_object_or_404(Reservar, pk=pk)
    if request.method == "POST":
        form = ReservacionForm(request.POST, instance=edireser)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('reservar.views.detalle_reservacion', pk=post.pk)
    else:
        form = ReservacionForm(instance=edireser)
    return render(request, 'reservar/editar_reservacion.html', {'form': form})
# Cdef reservar_hab(request, pk):
# C	inst = get_object_or_404(Habitacion, pk=pk)
# C    if request.method == "POST":
   # C#     form = ReservarForm(request.POST)
       # C if form.is_valid():
          # C  post = form.save(commit=False)
            # Cpost.autor = request.user
            # Cpost.habitacion = inst
            # Cpost.save()
            # Creturn redirect('reservar.views.detalle_habitacion', pk=post.pk)
 # C   else:
    # C    form = HabitacionForm()
    # Creturn render(request, 'reservar/editar_habitacion.html', {'form': form})