from django.shortcuts import render,redirect, reverse
from .models import Project
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import ProjectForm

# Create your views here.

def portfolio(request):
    projects = Project.objects.all()

    page = request.GET.get('page',1)
    paginator = Paginator(projects,3)

    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    return render(request, "portfolio/portfolio.html",{'projects':projects})

def add_beats(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            description = form.cleaned_data.get("description")
            image = form.cleaned_data.get("image")
            link = form.cleaned_data.get("link")
            obj = Project.objects.create(
                title = title,
                description = description,
                image = image,
                link = link
            )
            obj.save()
            return redirect(reverse('portfolio')+ '?OK')
            #return redirect(to = 'cursos')
        else:
            return redirect(reverse('portfolio')+ '?FAIL')
    else:
        form = ProjectForm

    return render(request,"portfolio/add_beats.html",{'form':form})
