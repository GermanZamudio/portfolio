from django.db import models

class Habilidad(models.Model):
    NIVEL_CHOICES = [
        ('principiante', 'Principiante'),
        ('intermedio', 'Intermedio'),
        ('avanzado', 'Avanzado'),
    ]
    
    titulo = models.CharField(max_length=100)
    nivel = models.CharField(max_length=100, choices=NIVEL_CHOICES)
    tiempo_experiencia = models.CharField(max_length=100)
    logo = models.ImageField()

    def __str__(self):
        return self.titulo



class Proyecto(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    tecnologias = models.ManyToManyField(
        'Habilidad', 
        related_name='proyecto',
        blank=True)
    enlace = models.URLField()
    imagen = models.ImageField(upload_to='proyectos/')  # Corregido: especificar upload_to para ImageField
    fecha = models.DateTimeField()

    def __str__(self):
        return self.titulo


class AcercaDe(models.Model):
    nombre = models.CharField(max_length=100)
    texto = models.TextField()
    imagen = models.ImageField(upload_to='acercade/')  # Corregido: especificar upload_to para ImageField

    def __str__(self):
        return self.nombre
