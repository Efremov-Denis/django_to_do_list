from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
       if request.method == 'POST':
           form = RegisterForm(request.POST)
           if form.is_valid():
               form.save()
               return redirect('login')  # Перенаправить на страницу входа после успешной регистрации
       else:
           form = RegisterForm()
       return render(request, 'register.html', {'form': form})