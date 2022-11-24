from django.http import HttpResponse
from django.shortcuts import render, reverse
from os import listdir, curdir
from os.path import isfile, abspath
from datetime import datetime
from pprint import pprint


def home_view(request):
    """
    Функция формирования контекста для заглавной страницы

    :param request:
    :return:
    """
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    """
    Функция формирования HTTP-ответа содержащего указание текущего времени
    """
    current_time = datetime.now().strftime("%H:%M:%S")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)

def make_dir_content()->dict:
    """
    Функция формирования словаря с содержанием рабочей папки

    Словарь формируется из списка файлов, списка директорий и
    абсолютного пути до рабочей папки

    :return:
    """
    content = {}
    content['files'] = []
    content['dirs'] = []
    for f in listdir():
        if isfile(f):
            content['files'].append(f)
        else:
            content['dirs'].append(f)
    dir_path = abspath(curdir)
    content['dir_path'] = dir_path
    return content

def workdir_view(request):
    """
    Функция формирования контекста для страницы, выводящей содержание
    рабочей папки

    :param request:
    :return:
    """
    template_name = 'app/workdir.html'
    content = make_dir_content()
    context = content
    return render(request, template_name, context)