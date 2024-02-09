from django.urls import path
from . import views
from .views import UserRegistration, PetRegistration, UploadPhotos
# from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='home'),
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reg_user/', UserRegistration.as_view(), name='user'),
    path('reg_pet/', PetRegistration.as_view(), name='pet'),
    path('upload_photo/', UploadPhotos.as_view(), name='photo'),

]
