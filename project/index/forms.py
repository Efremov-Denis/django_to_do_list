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

        widgets = {
            'completed': forms.CheckboxInput(attrs={'id': 'completed_checkbox', 'data-initial-value': False}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Название задачи'
        self.fields['description'].label = 'Описание задачи'
        self.fields['completed'].label = 'Завершено'
        if self.instance and self.instance.pk:  # Если это существующая задача
            self.fields['completed'].widget.attrs['data-initial-value'] = self.instance.completed