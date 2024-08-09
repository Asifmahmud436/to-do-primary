from django.shortcuts import render,redirect
from tasks.forms import TaskForm
from tasks.models import Task
# Create your views here.
def add_tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm()
    return render(request,'add_tasks.html',{'form':form})

def edit_tasks(request,id):
    task = Task.objects.get(pk=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance = task)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'add_tasks.html',{'form':form})

def delete_tasks(request,id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect('home')