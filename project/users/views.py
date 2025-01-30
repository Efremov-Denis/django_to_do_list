from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Сохраняем пользователя
            login(request, user)  # Автоматически логиним пользователя
            return redirect('task_list')  # Перенаправляем на главную страницу
        else:
            return render(request, 'register.html', {'form': form}) #Исправлено: Передаём форму с ошибками
    else: # Добавили ветку else для обработки GET запросов
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

def user_logout(request):
    if request.method == 'POST': # Если метод POST
        logout(request)
        return redirect('task_list') 
    else:
       return redirect('task_list') 