from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import *

# Create your views here.
def index(request):
   
    task = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/tasks')



    context = {'task': task,
     'form': form}
    return render(request, 'list_task.html', context)


def updata_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/tasks')

    context = {
        'form': form
    }

    return render(request, 'update.html', context) 

def delete_task(request, pk):
    item = Task.objects.get(id=pk)
    
    if request.method == "POST":
        item.delete()
        return redirect('/tasks')

    context = {'item': item}
    return render(request, 'delete_task.html', context)