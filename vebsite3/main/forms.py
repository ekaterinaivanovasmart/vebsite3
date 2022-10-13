from . models import Task
from django.forms import ModelForm, TextInput,Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task #указываем с какой моделью работаем
        fields = ["title", "task"] #указ-м какие поля должны быть в форме
        widgets = {
            "title": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите название задачи:'
            }),
            "task": Textarea(attrs={
                'class':'form-control',
                'placeholder':'Введите описание задачи:'}),
        } # Textarea - чтобы форма была большая

