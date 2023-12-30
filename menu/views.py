from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import Task_form
from .models import Task


def task(request):
    task = Task.objects.filter(user=request.user)
    context = {
        "title": "To-do List Website",
        "tasks": task,
    }
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context, request))


def create_task(request):
    if request.method == "POST":
        form = Task_form(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task")
    else:
        form = Task_form()

    context = {
        "title": "Create Task",
        "form": form,
    }
    template = loader.get_template("create_task.html")
    return HttpResponse(template.render(context, request))


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == "POST":
        form = Task_form(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task")
    else:
        form = Task_form(instance=task)

    context = {
        "title": "Edit Task",
        "form": form,
        "task": task,
    }
    template = loader.get_template("edit_task.html")
    return HttpResponse(template.render(context, request))


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.user == task.user:
        task.status = "Selesai"
        task.save()
        return redirect("task")
    else:
        return render(request, "Akses ditolak!")


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.user == task.user:
        task.delete()
        return redirect("task")
    else:
        return render(request, "Akses ditolak!")


def user_logout(request):
    logout(request)
    return redirect("user-login")
