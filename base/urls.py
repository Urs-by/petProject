from django.urls import path
from . import views
from .views import UserRegistration, PetRegistration


urlpatterns = [
    path('', views.index, name='index'),
    path('user_registration/', UserRegistration.as_view(), name='user'),
    path('pet_registration/', views.PetRegistration.as_view(), name='pet'),

]
