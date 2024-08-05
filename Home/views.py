from django.shortcuts import render
from .models import Habilidad, Proyecto, Contacto

def portfolio_view(request):
    habilidades = Habilidad.objects.all()
    proyectos = Proyecto.objects.all()
    contacto = Contacto.objects.first()  # Asumimos que solo hay un contacto

    context = {
        'habilidades': habilidades,
        'proyectos': proyectos,
        'contacto': contacto,
    }
    return render(request, 'home/portfolio.html', context)