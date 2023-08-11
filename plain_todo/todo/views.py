from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View

from .models import Task
# Create your views here.


class TasksView(View):

    def get(self, request):
        tasks_remaining = Task.objects.filter(isCompleted=False).order_by('-date_created')
        tasks_completed = Task.objects.filter(isCompleted = True)

        context = {
            'tasks_remaining': tasks_remaining,
            'tasks_completed': tasks_completed
        }
        return render(request, 'index.html', context = context)

    def post(self, request):
        task_text = request.POST.get('task')
        try:
            task = Task(text=task_text)
            task.save()
            return redirect('tasks')
        except Exception:
            return HttpResponse(Exception)
        
        


class EditTask(View):

    def post(self, request, pk):

        try:

            task = Task.objects.get(id=pk)
            task.isCompleted = True
            task.save()
            return redirect('tasks')
        except Exception:
            return HttpResponse(Exception)



def deleteTask(request, pk):

    if request.method == "POST":
        task = Task.objects.filter(id=pk)

        if task.exists():
            task.delete()
            return redirect('tasks')



