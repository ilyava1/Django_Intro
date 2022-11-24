from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
import csv
from django.core.paginator import Paginator


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    """
    Функция подготовки контекста для страницы с перечнем остановок
    """
    template = 'stations/bus_stations.html'
    path = BUS_STATION_CSV  # из settings получаем пусть к CSV-файлу
    with open(path, 'r', encoding = 'utf-8') as f: #
        reader = csv.reader(f)
        bs_list = list(reader)  # читаем файл в список остановок
    header = bs_list.pop(0)  # извлекаем заголовочную часть чтобы не мешала
    # if len(bs_list)%10:
    #     page_qua = len(bs_list) // 10 + 1
    # else:
    #     page_qua = len(bs_list) / 10
    #  далее получаем номер страницы из параметров запроса
    page_number = int(request.GET.get('page', 1)) # 1 - значение по умолчанию
                                                  # т.е. если стр не указана
                                                  # берем стр №1
    paginator = Paginator(bs_list, 10)
    page_qua = paginator.num_pages

    page = paginator.get_page(page_number)
    context = {
        'page': page,
        'page_qua': page_qua,
        }
    return render(request, template, context)
