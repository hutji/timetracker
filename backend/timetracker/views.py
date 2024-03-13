import datetime

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from .models import Task


def index(request):
    tasks = Task.objects.all()
    return render(request, "tracker/index.html", {"tasks": tasks})


@csrf_protect
def start_task(request):
    if request.method == "POST":
        task_name = request.POST.get("task_name")
        task = Task.objects.create(name=task_name, start_time=datetime.datetime.now())
        return JsonResponse({"task_id": task.id})


@csrf_protect
def end_task(request):
    if request.method == "POST":
        task_id = request.POST.get("task_id")
        task = Task.objects.get(id=task_id)
        task.end_time = datetime.datetime.now()
        task.save()
        return JsonResponse({})
