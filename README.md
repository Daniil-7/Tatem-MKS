# Tatem МКС
![Image alt](https://res.cloudinary.com/tatemmedia/image/upload/v1641548220/log1.jpg.jpg)
---
## Описание 
МКС Tatem - это агрегат контент(площадка которая собирает информацию с других ресурсов) о МКС и NASA. [Ссылка на сайт](https://tatemmks.herokuapp.com)
---
## Мотивация создание 
1. Вдохновение космосом.
2. Проект в портфолио с парсингом.
---
## Инструкция по запуску
1. Скопируйте репозиторий, установите зависимость и запустите:
```bash
git clone https://github.com/Daniil-7/Tatem-MKS.git
cd Tatem-MKS
pip install -r requirements.txt
python manage.py runserver
```
2. При диплои проекта не забудьте установить ключ:
файл ./gettingstarted/settings.py:
```python
SECRET_KEY = "ваш ключ"
```
---
## Использованные технологии
1. Python 3.10.2
2. Django 4.0
3. translators 4.11.3
4. beautifulsoup4 4.10.0
5. requests 2.26.0
6. gunicorn 20.1.0
---
## Примичание 
1. [Ссылка на сайт проекта](https://tatemmks.herokuapp.com)
2. [Сайт портфолио](https://tatem.pythonanywhere.com)
