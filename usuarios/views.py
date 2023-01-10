
from django.shortcuts import get_object_or_404, redirect, render

from usuarios.forms import AgentForm, Champ, PersonaNueva, Calculadora
from usuarios.models import Agent, User
import datetime

# Create your views here.

def detallePersona(request, id):
    persona = get_object_or_404(User, pk=id)
    
    return render(request,'perfiles/perfil.html',{'persona':persona})

#PersonaNueva = modelform_factory(User, exclude=[])
#CarreraNueva = modelform_factory(Career, exclude=[])

def nuevaPersona(request):
    if request.method == 'POST':
        nuevo = PersonaNueva(request.POST)
        if nuevo.is_valid():
            nuevo.save()
            return redirect('index')

    else:   
        nuevo = PersonaNueva()
    

    return render(request, 'perfiles/nueva_persona.html', {'nuevo':nuevo})


def favChamp(request):
     if request.method == 'POST':
        campeon = Champ(request.POST)
        if campeon.is_valid():
            campeon.save()
            return redirect('index')

     else:
          campeon = Champ()
    
     return render(request, 'perfiles/champfav.html', {'campeon':campeon})


def editarPersona(request, id):
    nuevo = get_object_or_404(User, pk=id)

    if request.method == 'POST':
        personaForm = PersonaNueva(request.POST, instance=nuevo)
        if personaForm.is_valid():
            personaForm.save()
            return redirect('index')

    else:   
        personaForm = PersonaNueva(instance=nuevo)

    return render(request, 'perfiles/editar_persona.html', {'personaForm':personaForm, 'nuevo':nuevo})


def eliminarPersona(request, id):
    persona = get_object_or_404(User, pk=id)

    if persona:
        persona.delete()
        return redirect('index')

def paondevaperro(request):
    return redirect('valindex')




def agentsIndex(request):
    agente = Agent.objects.all()
    
    
    return render(request, 'Valorant/agent_index.html', {'agente':agente})




def addAgent(request):
     if request.method == 'POST':
        agente = AgentForm(request.POST, request.FILES)
        if agente.is_valid():
            agente.save()
            return redirect('valindex')

     else:
          agente = AgentForm()
    
     return render(request, 'Valorant/newagent.html', {'agente':agente})


def agenteInfo(request, agent):
    #agente = Agent.objects.(agent)
    agente = get_object_or_404(Agent, pk=agent)
    hora = datetime.datetime.today()

    #agente_imagen = Agent.objects.all()

    

    #agente = get_object_or_404(Agent, pk=id)
    return render(request,'Valorant/agent_info.html', {'agente':agente, 'hora':hora} )


def navBar(request):
    hora = datetime.date.today()
    return render(request, 'perfiles/Bases/base1.html', {'hora':hora} )



def miCalculadora(request):
    hora = datetime.datetime.today()
    calculator = Calculadora()

    
    return render(request, 'PRUEBAS/calculator.html', {'calculator':calculator, 'hora':hora})


def pruebasManza(request):
    agentes = Agent.objects.all()
    return render(request, 'PRUEBAS/pruebas.html', {'agentes':agentes,})








            
            



    