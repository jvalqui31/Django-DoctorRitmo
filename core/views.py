from django.shortcuts import render, HttpResponse, redirect, reverse, HttpResponseRedirect


# Create your views here.

def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def docentes(request):
    return render(request, "core/docentes.html")
         
    

