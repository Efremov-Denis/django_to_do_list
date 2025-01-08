from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),  # URL для получения списка задач
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('index/<int:pk>/update/', views.TaskUpdateView.as_view(), name='task_update'),  # URL для обновления задачи
    path('index/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),  # URL для удаления задачи
]