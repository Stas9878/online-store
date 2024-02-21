from django.shortcuts import render

def login(request):
    context = {
        'title': 'O.Lib - Авторизация'
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'O.Lib - Регистрация'
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        'title': 'O.Lib - Мой профиль'
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    pass
