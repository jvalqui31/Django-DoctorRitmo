from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(verbose_name="Título",max_length=100)
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen",upload_to="projects")
    link = models.URLField(verbose_name="Sitio Web",null=True,blank=True)
    created = models.DateTimeField(verbose_name="Fecha creación",auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha actualización",auto_now=True)

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title