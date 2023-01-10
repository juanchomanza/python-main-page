from django.shortcuts import render
from usuarios.models import User


# Create your views here.

def bienvenido(request):

    contador = User.objects.count()
    usuarios = User.objects.all()
    userr= User.objects.order_by('career')

    return render(request, 'index.html', {
        'contador':contador, 'usuarios':usuarios, 'userr':userr,

    })


