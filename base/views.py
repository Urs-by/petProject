from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import User
from .forms import UserForm, PetForm

import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return render(request, "base/base.html")


class UserRegistration(View):
    def get(self, request):
        message = 'Регистрация '
        form = UserForm()
        return render(request, 'base/user_registration.html', context={'form': form, 'message': message})

    def post(self, request):
        form = UserForm(request.POST, request.FILES)
        message = 'Регистрация не выполнена!'
        if form.is_valid():
            name = form.cleaned_data['login']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            pet = form.cleaned_data['pets']
            city = form.cleaned_data['city']
            if pet:
                return redirect('../pet_registration/')
            else:
                # # Создание пользователя на основе введенных данных
                # user = form.save(commit=False)
                # # Дополнительные операции с данными пользователя, если необходимо
                # user.save()
                message = 'Регистрация прошла успешно!'
                context = {'form': form, 'message': message}
                return render(request, 'base/user_registration.html', context)

        return render(request, 'base/user_registration.html', {'form': form, 'message': message})


class PetRegistration(View):
    def get(self, request):
        message = 'Регистрация питомца'
        form = PetForm()
        return render(request, 'base/pet_registration.html', context={'form': form, 'message': message})

    def post(self, request):
        form = PetForm(request.POST, request.FILES)
        message = 'Регистрация не выполнена!'
        if form.is_valid():
            nickname = form.cleaned_data['nickname']
            breed = form.cleaned_data['breed']
            age = form.cleaned_data['age']
            # # Создание пользователя на основе введенных данных
            # user = form.save(commit=False)
            # # Дополнительные операции с данными пользователя, если необходимо
            # user.save()
            message = 'Регистрация прошла успешно!'
            context = {'form': form, 'message': message}
            return render(request, 'base/pet_registration.html', context)
