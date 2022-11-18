from django.http import HttpResponse
from django.shortcuts import render, reverse
from os import listdir
from os.path import isfile
from datetime import datetime


def home_view(request):
    template_name = 'app/home.html'

    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.now().strftime("%H:%M:%S")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей
    # директории

    fl = 0
    dir = 0
    msg = 'Содержание рабочей директории. '
    Files = ''
    Dirs = ''
    for f in listdir():
        if isfile(f):
            if fl == 0:
                Files += ' Файлы: ' + str(f)
                fl = 1
            else:
                Files += '; ' + str(f)
        else:
            if dir == 0:
                Dirs += 'Папки: ' + str(f)
                dir = 1
            else:
                Dirs += '; ' + str(f)
    msg += Dirs + Files
    return HttpResponse(msg)
