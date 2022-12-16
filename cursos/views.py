from django.shortcuts import render,redirect, reverse
from .models import Curso
from .forms import CursoForm

# Create your views here.
def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "cursos/cursos.html",{'cursos':cursos})

def add(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            idCurso = form.cleaned_data.get("idCurso")
            descripcion = form.cleaned_data.get("descripcion")
            precio = form.cleaned_data.get("precio")
            stock = form.cleaned_data.get("stock")
            imagen = form.cleaned_data.get("imagen")
            docente = form.cleaned_data.get("docente")
            obj = Curso.objects.create(
                idCurso = idCurso,
                descripcion = descripcion,
                precio = precio,
                stock = stock,
                imagen = imagen,
                docente = docente
            )
            obj.save()
            return redirect(reverse('add_curso')+ '?OK')
            #return redirect(to = 'cursos')
        else:
            return redirect(reverse('add_curso')+ '?FAIL')
    else:
        form = CursoForm

    return render(request,"cursos/add_curso.html",{'form':form})

def modificar_curso(request,idCurso):
    curso = Curso.objects.get(idCurso = idCurso)
    form = CursoForm(instance = curso)

    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance = curso)
        if form.is_valid():
            form.save()
            return redirect(reverse('cursos')+ "?OK")
        else:
            return redirect(reverse('mod_curso')+ idCurso)
    return render(request,"cursos/mod_curso.html",{'form':form})

def del_curso(request,idCurso):
    curso = Curso.objects.get(idCurso = idCurso)
    curso.delete()
    return redirect(to='cursos')

def cursos_publicos(request):
    cursos = Curso.objects.all()
    return render(request, "cursos/cursos-publicos.html",{'cursos':cursos})