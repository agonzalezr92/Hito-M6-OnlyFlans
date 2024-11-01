from django.shortcuts import render, redirect
from .models import Flan
from django.http import HttpResponseRedirect
from .forms import ContactFormModelForm
from .models import ContactForm
from django.urls import reverse


# Create your views here.

# views.py

def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'web/index.html', {"flanes": flanes_publicos})

def about(request):
    datos_empresa = {
        "descripcion": "Tienda en línea dedicada a la creación de postres gourmet hechos a mano, donde cada flan es elaborado con los mejores ingredientes y un toque de pasión. Desde el clásico Flan de Caramelo hasta opciones exóticas como el Flan de Maracuyá y el Flan de Frambuesa, nuestros postres ofrecen una experiencia deliciosa y única que transforma cualquier ocasión en un momento especial. Disfruta de la suavidad y los sabores vibrantes de nuestros flanes, perfectos para consentirte o sorprender a tus seres queridos. ¡Haz tu pedido hoy y déjate llevar por la dulzura de OnlyFlans!",
        "fecha_creacion": "2021",
        "ubicacion": "Santiago, Chile"
    }
    return render(request, 'web/about.html', {"datos_empresa": datos_empresa})


def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'web/welcome.html', {"flanes": flanes_privados})


def contacto(request):
    if request.method == "POST":
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exito')  # Asegúrate de tener configurada esta ruta
    else:
        form = ContactFormModelForm()

    return render(request, 'web/contacto.html', {'form': form})

def exito(request):
    return render(request, 'web/exito.html')