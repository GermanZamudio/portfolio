from django.contrib import admin
from .models import Habilidad,Proyecto,AcercaDe

admin.site.register(Proyecto)
admin.site.register(AcercaDe)
admin.site.register(Habilidad)