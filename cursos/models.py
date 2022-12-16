from django.db import models

# Create your models here.

class Docente(models.Model):
    idDocente = models.IntegerField(primary_key=True, verbose_name='ID')
    docente = models.CharField(max_length=50,verbose_name='Docente')

    class Meta:
        verbose_name='docente'
        verbose_name_plural='docentes'
        ordering = ['docente']
    
    def __str__(self):
        return self.docente

class Curso(models.Model):
    idCurso = models.CharField(primary_key=True,max_length=10,verbose_name='ID')
    descripcion = models.CharField(max_length=100,verbose_name='Descripción')
    precio = models.IntegerField(verbose_name='Precio Unitario')
    stock = models.IntegerField(verbose_name='Stock')
    imagen = models.ImageField(verbose_name='Imagen',upload_to='cursos',null=True,blank=True)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    class Meta:
        verbose_name='curso'
        verbose_name_plural='cursos'
        ordering = ['descripcion']
    
    def __str__(self):
        return self.descripcion
