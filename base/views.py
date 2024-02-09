from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View
from .models import UserCustom, Pet, PetPhoto
from .forms import UserCustomForm, PetForm, PetPhotoForm


import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return render(request, "base/home.html")


class UserRegistration(View):
    def get(self, request):
        message = 'Регистрация '
        form = UserCustomForm()
        return render(request, 'registration/user_registration.html', context={'form': form, 'message': message})

    def post(self, request):
        form = UserCustomForm(request.POST, request.FILES)
        message = 'Регистрация не выполнена!'
        # new_user = UserCustom()
        if form.is_valid():
            user = form.save()
            pets = form.cleaned_data['pets']
            city = form.cleaned_data['city']
            image = form.cleaned_data['image']
            UserCustom.objects.create(user=user, pets=pets, city=city, image=image)
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            message = 'Вы успешно зарегистрированы!'
            context = {'form': form, 'message': message}
            return render(request, 'base/base.html', context)

        return render(request, 'registration/user_registration.html', {'form': form, 'message': message})
    #


class PetRegistration(View):
    def get(self, request):
        message = 'Регистрация питомца'
        form = PetForm()
        return render(request, 'registration/pet_registration.html', context={'form': form, 'message': message})


    def post(self, request):
        if request.user.is_authenticated:
            form = PetForm(request.POST)
            message = 'Регистрация не выполнена!'
            if form.is_valid():
                nickname = form.cleaned_data['nickname']
                breed = form.cleaned_data['breed']
                age = form.cleaned_data['age']
                user_custom = request.user.usercustom
                pet = Pet.objects.create(nickname=nickname, breed=breed, age=age)
                pet.owners.add(user_custom.user)
                logger.info('Pet is registered')
                message = 'Регистрация Вашего питомца прошла успешно!'
                context = {'message': message}
                return render(request, 'base/add_photo.html', context)
        else:
            return redirect('login')


class UploadPhotos(View):
    def get(self, request):
        message = 'Загрузка фото'
        form = PetPhotoForm()
        return render(request, 'base/upload_photo.html', {'form': form, 'message': message})
# class UploadPhotos(View):
#     def get(self, request):
#         form = PetPhotoForm()
#         return render(request, 'base/add_photo.html', {'form': form})

# def post(self, request, pet_id):
#    your_pet_instance = Pet.objects.get(id=pet_id)
#    form = PetPhotoForm(request.POST, request.FILES)
#    if form.is_valid():
#        for image in request.FILES.getlist('images'):
#            pet_photo = PetPhoto(pet=your_pet_instance, image=image)
#            pet_photo.save()
#        return redirect('success_url')
#    else:
#        form = PetPhotoForm()
#    return render(request, 'base/upload_photo.html', {'form': form})
