"""sap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from usuarios.views import addAgent, agenteInfo, agentsIndex, detallePersona, eliminarPersona, favChamp, miCalculadora, navBar, nuevaPersona, editarPersona, paondevaperro, pruebasManza
from webapps.views import bienvenido
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', bienvenido, name='index'),
    path('', bienvenido, name='index'),
    path('perfil/<int:id>', detallePersona,),
    path('nueva_persona/', nuevaPersona, name='add'),
    path('editar_persona/<int:id>', editarPersona),
    path('champfav/', favChamp, name='champ'),
    path('eliminar_persona/<int:id>', eliminarPersona),
    path('agent_index/', agentsIndex, name='valindex'),
    path('add_agent/', addAgent, name='valadd'),
    path('agent_index/agent/<agent>', agenteInfo),
    path('agent_index/agent/', paondevaperro),
    path('agent_index/agent', paondevaperro),
    path('calculator/', miCalculadora, name='calcu'),
    path('pruebas/', pruebasManza),
    path('blog/', include('blog.urls')),
    path('', include('User.urls'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

urlpatterns += staticfiles_urlpatterns()


