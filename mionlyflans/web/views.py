from django.shortcuts import render

# Create your views here.

# views.py

def index(request):
    productos = [
        {"nombre": "Flan de Caramelo", "precio": "$10.000", "descripcion": "Este delicioso flan de caramelo tiene una textura suave y cremosa, acompañado de una capa de caramelo dorado que se derrite en la boca. Perfecto para quienes buscan un postre clásico con un toque irresistible de dulzura.", "imagen": "images/imagen1.jpg"},
        {"nombre": "Flan Maracuyá", "precio": "$15.000", "descripcion": "Exótico y refrescante, este flan de maracuyá combina la suavidad del flan con el sabor tropical de la fruta de la pasión. Su equilibrio entre dulce y ácido lo convierte en una experiencia deliciosa e inolvidable.", "imagen": "images/imagen2.jpg"},
        {"nombre": "Flan Frambuesas", "precio": "$8.000", "descripcion": "Un postre delicado y vibrante, el flan de frambuesa sorprende con su color y sabor únicos. Con un toque afrutado y suave, es la elección ideal para quienes aman los postres ligeros y llenos de sabor.", "imagen": "images/imagen3.jpg"},
    ]
    return render(request, 'web/index.html', {"productos": productos})

    return render(request, 'web/index.html', {"productos": productos})

def about(request):
    datos_empresa = {
        "descripcion": "Tienda en línea dedicada a la creación de postres gourmet hechos a mano, donde cada flan es elaborado con los mejores ingredientes y un toque de pasión. Desde el clásico Flan de Caramelo hasta opciones exóticas como el Flan de Maracuyá y el Flan de Frambuesa, nuestros postres ofrecen una experiencia deliciosa y única que transforma cualquier ocasión en un momento especial. Disfruta de la suavidad y los sabores vibrantes de nuestros flanes, perfectos para consentirte o sorprender a tus seres queridos. ¡Haz tu pedido hoy y déjate llevar por la dulzura de OnlyFlans!",
        "fecha_creacion": "2021",
        "ubicacion": "Santiago, Chile"
    }
    return render(request, 'web/about.html', {"datos_empresa": datos_empresa})

def welcome(request):
    usuario = {"nombre": "Bryan Diaz"}  # Simula un usuario autenticado
    return render(request, 'web/welcome.html', {"usuario": usuario})


