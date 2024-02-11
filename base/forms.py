from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Pet


class UserCustomForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserCustomForm, self).__init__(*args, **kwargs)
        # Отключаем сообщения о критериях сложности пароля
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    city = forms.CharField(label="Город", required=False)
    pets = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label="Питомцы")
    image = forms.ImageField(widget=forms.ClearableFileInput(), required=False, label="Можете загрузить свое фото")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'city', 'pets', 'image')


class PetForm(forms.Form):
    nickname = forms.CharField(max_length=50, label="Кличка")
    breed = forms.CharField(max_length=50, label="Порода")
    age = forms.IntegerField(label="Возраст", max_value=30, required=False)


class PetPhotoForm(forms.Form):
    image = forms.ImageField(widget=forms.ClearableFileInput(), required=False,
                             label="Здесь Вы можете загрузить фото своего питомца")
    comment = forms.CharField(widget=forms.Textarea(), required=False, label="Комментарии")


