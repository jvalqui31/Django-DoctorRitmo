from django.shortcuts import render, HttpResponse, redirect, reverse, HttpResponseRedirect
from .models import Contacto

# Create your views here.

def contact(request):
    if request.method=="POST":
        contacto=Contacto()
        name = request.POST.get('name')
        rut = request.POST.get('rut')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        email = request.POST.get('email')
        password = request.POST.get('password')
        genero = request.POST.get('genero')
        instrumento = request.POST.get('instrumento')
        comuna = request.POST.get('comuna')
        comentarios = request.POST.get('comentarios')
        contacto.name = name
        contacto.rut = rut
        contacto.fecha_nacimiento = fecha_nacimiento
        contacto.email = email
        contacto.password = password
        contacto.genero = genero
        contacto.instrumento = instrumento
        contacto.comuna = comuna
        contacto.comentarios = comentarios
        contacto.save()        
        return HttpResponseRedirect("/contact/?OK")   
    return render(request, "contact/contact.html")

def listar_contactos(request):
    form = Contacto.objects.all()
    return render(request, "contact/listar-contactos.html",{'contact':form})