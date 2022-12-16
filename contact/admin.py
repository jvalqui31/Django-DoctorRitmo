from django.contrib import admin
from .models import Contacto

# Register your models here.
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('name', 'rut', 'fecha_nacimiento','genero','comentarios')
 

admin.site.register(Contacto, ContactoAdmin)
