Домашний проект# PetUnfriendly Places Map

PetUnfriendly Places Map - это веб-приложение на Django, которое отображает на карте места, где запрещен вход с собаками.
Зарегистрированные пользователи могут добавлять метки на карту, 
указывать название магазина и оставлять комментарии по причинам отказа во входе с собакой.
Также могут загружать фото своих питомцев для общей галлереи

## Установка

1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/Urs-by/petProject
   cd petunfriendly-places-map
   ```

2. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Примените миграции:

   ```bash
   python manage.py migrate
   ```

4. Запустите сервер разработки:

   ```bash
   python manage.py runserver
   ```

5. Перейдите по адресу http://127.0.0.1:8000/ в вашем браузере.

## Использование

1. Зарегистрируйте новых пользователей или войдите в свой аккаунт.

2. Добавьте новое место на карту, указав название магазина и причину отказа во входе с собакой.

3. Просматривайте метки на карте с комментариями других пользователей.

4. Загружайте фотографии своих питомцев в общую галерею.

## Вклад в проект

Мы приветствуем любые вклады в проект. Если у вас есть предложения по улучшению функционала, исправлению ошибок или другие идеи, пожалуйста, создавайте pull requests.

## Лицензия

Этот проект распространяется под лицензией MIT. Подробности смотрите в файле LICENSE.

## Дополнительная информация

- Версия Python: 3.x
- Версия Django: 3.x

PetUnfriendly Places Map - ваш надежный помощник в поиске мест, куда лучше не водить ваших пушистых друзей! 🐶🚫

Если у вас есть вопросы, идеи или предложения, не стесняйтесь обращаться. Рады помочь!