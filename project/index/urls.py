from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),  # URL для получения списка задач
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
]