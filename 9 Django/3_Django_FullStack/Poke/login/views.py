from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from time import gmtime, strftime
import bcrypt

from .models import *

# Create your views here.
# si no existe, se debe  crear la carpeta templates en la application
# ademas crear los archivos html
def login(request):
    return render(request, 'registro.html')

def registrar(request):
    return render(request, 'registro.html')

def inicio(request):
    usuario = User.objects.filter(email=request.POST['email2'])
    errores = User.objects.validar_login(request.POST, usuario)

    if len(errores) > 0:
        for key, msg in errores.items():
            messages.error(request, msg)
        return redirect('/')
    else:
        request.session['user_id'] = usuario[0].id
        return redirect('home/')

def registro(request):
    #validacion de parametros
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('/registrar')

    else:
        #encriptar password
        password = User.objects.encriptar(request.POST['password'])
        decode_hash_pw = password.decode('utf-8')
        
        rol = 2
        if User.objects.all().count() ==0:
            rol = 1
        #crear usuario
        user = User.objects.create(
        nombre=request.POST['nombre'],
        alias=request.POST['alias'],
        email=request.POST['email'],
        cumple=request.POST['cumple'],
        password=decode_hash_pw,
        rol=rol,
        )
        msg="Usuario creado exitosamente!"
        messages.success(request, msg)
        #request.session['user_id'] = user.id  #para que se logue inmediatamente
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')
