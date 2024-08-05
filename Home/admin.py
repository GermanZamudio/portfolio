from django.contrib import admin
from .models import Habilidad, Proyecto, Contacto

class HabilidadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'nivel', 'tiempo_experiencia')
    search_fields = ('titulo', 'nivel')

class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'enlace')
    search_fields = ('titulo', 'tecnologias__titulo')
    list_filter = ('fecha', 'tecnologias')
    filter_horizontal = ('tecnologias',)
    prepopulated_fields = {'titulo': ('descripcion',)}

class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono')
    search_fields = ('nombre', 'email', 'telefono')

admin.site.register(Habilidad, HabilidadAdmin)
admin.site.register(Proyecto, ProyectoAdmin)
admin.site.register(Contacto, ContactoAdmin)
