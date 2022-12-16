"""webpersonal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from portfolio import views as portfolio_views
from contact import views as contact_views
from cursos import views as cursos_views

from django.conf import settings #aqui importamos la ruta de setting para agregar los media

urlpatterns = [
    path('', core_views.home, name='home'),
    path('acerca-de/', core_views.about, name='about'),
    path('portfolio/', portfolio_views.portfolio, name='portfolio'),
    path('add_beats/', portfolio_views.add_beats, name='add_beats'),
    path('cursos-publicos/', cursos_views.cursos_publicos, name='cursos-publicos'),
    path('cursos/', cursos_views.cursos, name='cursos'),
    path('add_curso/', cursos_views.add, name='add_curso'),
    path('mod_curso/<idCurso>', cursos_views.modificar_curso, name='mod_curso'),
    path('del_curso/<idCurso>', cursos_views.del_curso, name='del_curso'),
    path('docentes/', core_views.docentes, name='docentes'),
    path('contact/', contact_views.contact, name='contact'),
    path('listar-contactos/', contact_views.listar_contactos, name='listar-contactos'),
    path('admin/', admin.site.urls),
]

#aqui es para llamar la ruta de las static media img
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
