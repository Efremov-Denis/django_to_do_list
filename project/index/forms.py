from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'title',
            'description',
            'completed',
        )
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Укажите имя задачи'
        self.fields['description'].label = 'Опишите вашу задачу'
        self.fields['completed'].label = 'Статус завершения'