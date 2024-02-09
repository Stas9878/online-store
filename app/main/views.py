from django.shortcuts import render

def index(request):
    context = {
        'title': 'Главная',
        'content': 'Something'
    }
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html')
