from django.urls import path
from . import views
from .views import UserRegistration


urlpatterns = [
    path('', views.index, name='index'),
    path('user_registration/', UserRegistration.as_view(), name='user'),

]
