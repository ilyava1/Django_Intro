from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def ingrs_multiplication(choisen_dish, servings):
    """
    Функция перемножения ингредиентов на количество персон

    :param choisen_dish: словарь с блюдами, ингридентами и их кол-ом
    :param servings: количество персон
    :return: словарь с блюдами, ингридентами и их кол-ом в расчета на
    количество персон servings
    """
    for key, item in choisen_dish.items():
        new_ingrs = {}
        for ingr, qua in item.items():
            new_ingrs[ingr] = qua * servings
        choisen_dish[key] = new_ingrs
    return choisen_dish


def home_view(request):
    """
    Функция формирования контекста для стартовой страницы сервиса
    :param request:
    :return: результат работы функции render
    """
    template_name = 'calculator/index.html'
    my_context = {}
    my_context['data'] = DATA
    context = my_context
    return render(request, template_name, context)


def prepare_dish(request, user_choise):
    """
    Функция формирования контекста для страницы блюда

    Функция формирует словарь choisen_dish из одной пары ключ-значение:
    блюдо-список_ингредиентов. Затем проверяет есть ли в запросе параметр
    servings - количество персон. Если нет, количество персон принимается
    за единицу, если есть - то данное значение извлекается. Далее choisen_dish
    и servings передается в функцию ingrs_multiplication для расчета кол-ва
    ингредиентов на заданное кол-во персон. Возращается словарь с перечнем и
    кол-ом ингредиентов, который вместе с шаблоном страницы передается в
    функцию render
    :param request:
    :return: результат работы функции render
    """
    template_name = 'calculator/recipes.html'
    my_context = {}
    choisen_dish = {}
    if user_choise in DATA.keys():
        choisen_dish[user_choise] = DATA[user_choise]

        if 'servings' in request.GET:
            servings = int(request.GET['servings'])
        else:
            servings = 1
        choisen_dish = ingrs_multiplication(choisen_dish, servings)
    else:
        choisen_dish[user_choise] = {}

    my_context['data'] = choisen_dish
    context = my_context

    return render(request, template_name, context)
