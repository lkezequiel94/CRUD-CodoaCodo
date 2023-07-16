from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length= 100, verbose_name="Titulo")
    descripcion = models.TextField(verbose_name="Descripcion")
    imagen = models.ImageField(verbose_name="Imagen", upload_to="projects")
    created = models.DateTimeField(auto_now_add = True, verbose_name="Fecha Creacion")
    updated = models.DateTimeField(auto_now = True, verbose_name="Fecha modificacion")

    def __str__(self):
        return self.title
    
class Meta:
    verbose_name = "proyecto"
    verbose_name_plural = "proyectos"
    ordering = ["-created"]