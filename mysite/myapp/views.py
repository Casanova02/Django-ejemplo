from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from .forms import CreateNewTask, CreateNewProject


# Create your views here.

def index(request):
    title='Django course'
    return render(request, 'index.html',{'title':title})

def hello(request,username):
    print(username)
    return HttpResponse("<h1>Hello World! %s</h1>" % username)

def about(request):
    user = 'Santiago'
    return render(request, 'about.html',{'user':user})

def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects':projects})

def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'Tasks/tasks.html',{'tasks':tasks})

def create_task(request):
    
    if request.method == 'GET':
        #Show interface
        return render(request, 'Tasks/create_task.html',{
        'form': CreateNewTask()
    })
    else:
        Task.objects.create(name = request.POST['name'],
        description = request.POST['description'], project_id = 1)
        return redirect('tasks')
    
def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html',{
            'form': CreateNewProject()})
    else:
        Project.objects.create(name = request.POST['name'])
        return redirect('projects')
        
        
    
