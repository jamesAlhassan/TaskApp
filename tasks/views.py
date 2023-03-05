from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def index(request):
    task = Task.objects.all()
    context = {'task': task}
    return render(request, 'base.html', context)