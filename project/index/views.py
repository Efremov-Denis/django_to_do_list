from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from .forms import TaskForm

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    template_name = 'task_create.html'
    form_class = TaskForm  # Используем TaskForm вместо fields
    success_url = reverse_lazy('task_list') # Укажите url на который перенаправить после создания задачи

#class TaskDetailView(DetailView):
#    model = Task
#    template_name = 'task_detail.html'
#    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'task_update.html'
    form_class = TaskForm  # Используем TaskForm вместо fields

    def get_success_url(self):
        return reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('task_list')

#def task_list(request):
#    tasks = Task.objects.all()
#    return render(request, 'index/task_list.html', {'tasks': tasks})

def task_toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = not task.completed
    task.save()
    return redirect('task_list') # Направляем в task_list