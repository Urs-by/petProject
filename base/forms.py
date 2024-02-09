from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Pet


class UserCustomForm(UserCreationForm):
    # login = forms.CharField(max_length=50, label="Логин")
    # password = forms.CharField(widget=forms.PasswordInput(), label="Пароль", min_length=5)
    # confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Подтвердите пароль", min_length=5)
    # email = forms.EmailField(widget=forms.EmailInput())
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

    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")
    #
    #     if password and confirm_password:
    #         if password != confirm_password:
    #             raise forms.ValidationError("Пароли не совпадают. Повторите попытку.")
    #
    #     return cleaned_data


class PetForm(forms.Form):
    nickname = forms.CharField(max_length=50, label="Кличка")
    breed = forms.CharField(max_length=50, label="Порода")
    age = forms.IntegerField(label="Возраст", max_value=30, required=False)


class PetPhotoForm(forms.Form):
    image = forms.ImageField(widget=forms.ClearableFileInput(), required=False, label="Здесь Вы можете загрузить фото своего питомца")
    comment = forms.CharField(widget=forms.Textarea(), required=False, label="Комментарии")
