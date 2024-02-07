from django import forms
from .models import User, Pet


class UserForm(forms.Form):
    login = forms.CharField(max_length=50, label="Логин")
    email = forms.EmailField(widget=forms.EmailInput())
    city = forms.CharField(label="Город", required=False)
    password = forms.CharField(widget=forms.PasswordInput(), label="Пароль", min_length=5)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Подтвердите пароль", min_length=5)
    pets = forms.BooleanField(widget=forms.CheckboxInput(), required=False, label="Питомцы")
    print(pets)
    image = forms.ImageField(widget=forms.ClearableFileInput(), required=False, label="Можете загрузить свое фото")


    # class Meta:
    #     model = User
    #     fields = ['login', 'email', 'city', 'pets',  'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError("Пароли не совпадают. Введите их заново.")

        return cleaned_data


class PetForm(forms.Form):

    nickname = forms.CharField(max_length=50, label="Кличка")
    breed = forms.CharField(max_length=50, label="Порода")
    age = forms.IntegerField(label="Возраст", max_value=30, required=False)
    # class Meta:
    #     model = Pet
    #     fields = ['nickname', 'breed', 'age']


