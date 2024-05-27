from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.template.loader import render_to_string


menu = [
        {'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'},
    ]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография', 'is_published': True},
    {'id': 2, 'title': 'Робби', 'content': 'Биография', 'is_published': False},
    {'id': 3, 'title': 'Джолий', 'content': 'Биография', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певецы'},
    {'id': 3, 'name': 'Спортсменки'},
]


def index(request):
    # t = render_to_string('Saratov/index.html')
    # return HttpResponse(t)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': 0,
    }
    return render(request, 'Saratov/index.html', context=data)


def about(request):
    return render(request, 'Saratov/about.html', {'title': 'О сайте', 'menu': menu})


def categories(request, cat_id):
    return HttpResponse(f"<h1>Страница по категориям</h1><p>id:{cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Страница по категориям</h1><p>slug:{cat_slug}</p>")


def show_post(request, post_id):
    return HttpResponse(f"отображение статьи с id = {post_id}")


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def show_category(request, cat_id):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'Saratov/index.html', context=data)



def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

