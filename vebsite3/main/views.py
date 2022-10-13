from django.shortcuts import render, redirect
from . models import Task
from .forms import TaskForm

def index(request):
    task = Task.objects.order_by('-id')#обращаемся к нашим данным в БД
    return render(request,'main/index.html',
                  {'title': 'Главная страница сайта',
                   'tasks': task}) # tasks для index.html для цикла for


def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':# для отправки и сохранения данных ч/з форму
        form = TaskForm(request.POST)
        if form.is_valid(): # проверяем форму на валидность(корректность заполнения)
            form.save() # save() сохраняем как новую запись  данных в БД(если они валидны)
            return redirect('home')
        else:
            error = 'Форма заполнена неверно!'
    form = TaskForm()
    context = {
        "form": form,
        "error": error
    }
    return render(request, 'main/create.html',context)


