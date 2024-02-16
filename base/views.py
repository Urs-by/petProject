from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View
from .models import UserCustom, Pet, PetPhoto, Shop, UserShopRating
from .forms import UserCustomForm, PetForm, PetPhotoForm, ShopForm, PetPhotoForm
from django.http import JsonResponse

import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return render(request, "base/home.html")


def show_map(request):
    # shops = Shop.objects.all()
    # data = [{'name': shop.shop_name, 'latitude': shop.coordinates_lat, 'longitude': shop.coordinates_lng,
    #          'rating': float(shop.total_rating)} for shop in shops if shop.coordinates_lat and shop.coordinates_lng]
    shops = UserShopRating.objects.select_related('shop').all()

    data = [{'name': shop.shop.shop_name, 'latitude': shop.shop.coordinates_lat, 'longitude': shop.shop.coordinates_lng,
             'rating': float(shop.users_rating), 'comment': shop.comment} for shop in shops if
            shop.shop.coordinates_lat and shop.shop.coordinates_lng]

    return render(request, 'base/home.html', {'data': data})


class UserRegistration(View):
    def get(self, request):
        message = 'Регистрация '
        form = UserCustomForm()
        return render(request, 'registration/user_registration.html', context={'form': form, 'message': message})

    def post(self, request):
        form = UserCustomForm(request.POST, request.FILES)
        message = 'Регистрация не выполнена!'
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


class SetRatingView(View):
    def get(self, request):
        message = 'Поставить оценку'
        form = ShopForm()
        context = {'form': form, 'message': message}
        return render(request, 'base/set_rating.html', context=context)

    def post(self, request):
        if request.user.is_authenticated:
            form = ShopForm(request.POST)
            message = 'Ваша оценка не сохранена!'
            if form.is_valid():
                latitude = form.cleaned_data['latitude']
                longitude = form.cleaned_data['longitude']
                shop_name = form.cleaned_data['shop_name']
                legal_name = form.cleaned_data['legal_name']
                city = form.cleaned_data['city']  #
                street = form.cleaned_data['street']
                users_rating = form.cleaned_data['user_rating']
                comment = form.cleaned_data['comment']
                review = Shop.objects.create(coordinates_lat=latitude, coordinates_lng=longitude, shop_name=shop_name,
                                             legal_name=legal_name, city=city, street=street)
                UserShopRating.objects.create(user=request.user, shop=review, users_rating=users_rating,
                                              comment=comment)
                logger.info('Rating is saved')
                message = 'Ваша оценка сохранена!'
                context = {'message': message}
                return render(request, 'base/base.html', context)
        return render(request, 'base/set_rating.html', {'form': form, 'message': message})


class ExitView(View):
    def get(self, request):
        return render(request, 'base/exit.html')


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

    def post(self, request):
        if request.user.is_authenticated:
            form = PetPhotoForm(request.POST, request.FILES)
            if form.is_valid():
                user = request.user
                image = form.cleaned_data['image']
                comment = form.cleaned_data['comment']
                PetPhoto.objects.create(pet=user, image=image, comment=comment)
                message = 'Фотография загружена'
                return render(request, 'base/my_pets.html', context={'message': message})
            else:
                return redirect('login')


class MyRatings(View):
    def get(self, request):
        message = 'Мои оценки'
        user = request.user
        ratings = UserShopRating.objects.filter(user=user)
        context = {'ratings': ratings, 'message': message}
        return render(request, 'base/my_ratings.html', context=context)


class MyPets(View):
    def get(self, request):
        message = 'Мои питомцы'
        user = request.user
        pets = Pet.objects.filter(owners=user)
        photos = PetPhoto.objects.filter(pet=user)
        context = {'pets': pets, 'photos': photos, 'my_range': range(3), 'message': message}
        return render(request, 'base/my_pets.html', context=context)


class Forum(View):
    def get(self, request):
        message = 'Форум'
        return render(request, 'base/forum.html', context={'message': message})


class About(View):
    def get(self, request):
        message = 'О проекте'
        return render(request, 'base/about.html', context={'message': message})
