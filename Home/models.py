from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

class Habilidad(models.Model):
    NIVEL_CHOICES = [
        ('principiante', _('Principiante')),
        ('intermedio', _('Intermedio')),
        ('avanzado', _('Avanzado')),
    ]
    
    titulo = models.CharField(max_length=100)
    nivel = models.CharField(max_length=20, choices=NIVEL_CHOICES)
    tiempo_experiencia = models.PositiveIntegerField(help_text=_("Experiencia en años"))
    logo = models.ImageField(upload_to='habilidades/', blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = _("Habilidad")
        verbose_name_plural = _("Habilidades")


class Proyecto(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    tecnologias = models.ManyToManyField(
        'Habilidad', 
        related_name='proyectos',
        blank=True
    )
    enlace = models.URLField()
    imagen = models.ImageField(upload_to='proyectos/', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha']
        verbose_name = _("Proyecto")
        verbose_name_plural = _("Proyectos")


class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    acercade = models.TextField()
    foto = models.ImageField(upload_to='acercade/', blank=True, null=True)
    telefono = PhoneNumberField()
    email = models.EmailField()
    git = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = _("Contacto")
        verbose_name_plural = _("Contactos")
