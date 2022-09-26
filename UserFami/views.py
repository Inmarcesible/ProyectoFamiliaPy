from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

from UserFami.forms import UserRegisterForm
from UserFami.models import Avatar


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data

            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user:
                login(request, user)
                messages.info(request, 'inicio de sesion satisfactorio!')

            else:
                messages.info(request, 'inicio de sesion fallido!')
        else:
            messages.info(request, 'Inicio sesion fallido')

        return redirect('AppFamiInicio')

    contexto = {
        'form': AuthenticationForm(),
        'name_submit': 'login'
    }
    return render(request, 'UserFami/login.html', contexto)


def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            #form.save()
            user = form.save()

            avatar = Avatar(user=user, imagen=form.cleaned_data.get('imagen'))
            avatar.save()

            messages.info(request, 'Tu usuario fue registrado satisfactoriamente!')
        else:
            messages.info(request, 'Tu usuario no puso ser registrado!')
        return redirect('AppFamiInicio')

    contexto = {
        #'form': UserCreationForm(),
        'form': UserRegisterForm(),
        'name_submit': 'Registrarse'
    }

    return render(request, 'UserFami/login.html', contexto)




