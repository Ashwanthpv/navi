from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
import csv
from .models import Task
from .forms import TaskForm

def download_tasks(request):
    tasks = Task.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="tasks.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Title', 'Client', 'Priority', 'Due Date', 'Completed'])
    for task in tasks:
        writer.writerow([task.id, task.title, task.client.full_name if task.client else '', task.priority, task.due_date, 'Yes' if task.completed else 'No'])
    
    return response

def tasks_list(request):
    tasks = Task.objects.all()
    return render(request, "tasks/tasks_list_mobile.html", {"tasks": tasks})

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/tasks/")
    else:
        form = TaskForm()
    return render(request, "tasks/add_task_mobile.html", {"form": form})

def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/tasks/")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/add_task_mobile.html", {"form": form})

def delete_task(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return redirect("/tasks/")
    return render(request, "tasks/delete_task.html", {"task": task})
