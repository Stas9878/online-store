from django.shortcuts import render
from goods.models import Categories


def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'O.LIB - Главная',
        'content': 'Онлайн магазин книг',
        'cat': categories,

    }
    return render(request, 'index.html', context=context)

def about(request):
    context = {
        'title': 'O.Lib - О нас',
        'content': 'О нас',
        'text_on_page': 'Крутой магазин книг'
    }
    return render(request, 'about.html', context=context)
