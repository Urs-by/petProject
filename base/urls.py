from django.urls import path
from . import views
from .views import (UserRegistration, PetRegistration, SetRatingView,
                    UploadPhotos, ExitView, MyRatings, MyPets, Forum, About)

# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='home'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('reg_user/', UserRegistration.as_view(), name='user'),
    path('set_rating/', SetRatingView.as_view(), name='rating'),
    path('exit/', ExitView.as_view(), name='exit'),
    path('reg_pet/', PetRegistration.as_view(), name='pet'),
    path('upload_photo/', UploadPhotos.as_view(), name='photo'),
    path('my_rating', MyRatings.as_view(), name='my_rating'),
    path('my_pets', MyPets.as_view(), name='my_pets'),
    path('forum', Forum.as_view(), name='forum'),
    path("about/", About.as_view(), name="about"),

]
