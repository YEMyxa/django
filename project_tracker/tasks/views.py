from django.http import HttpResponse
from django.urls import reverse
from .models import Project, Task

from django.shortcuts import render

def index(request):
    quality_control_url = reverse('quality_control:index')
    project_list_url = reverse('tasks:project_list')
    html = (f"<h1>Страница приложения tasks</h1>"
            f"<a href='{quality_control_url}'>Страница приложения quality_control</a></br>"
            f"<a href='{project_list_url}'>Список проектов</a>")
    return HttpResponse(html)

def project_list(request):
    projects = Project.objects.all()
    projects_html = '<h1>Список проектов</h1><ul>'
    for project in projects:
        projects_html += f'<li><a href="{project.id}/">{project.name}</a></li>'
    projects_html += '</ul>'
    return HttpResponse(projects_html)

from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'tasks/index.html')

from django.views.generic import ListView

class ProjectListView(ListView):
    model = Project
    template_name = 'tasks/projects_list.html'

from django.views.generic import DetailView

class ProjectDetailView(DetailView):
    model = Project
    pk_url_kwarg = 'project_id'
    template_name = 'tasks/project_detail.html'

class TaskDetailView(DetailView):
    model = Task
    pk_url_kwarg = 'task_id'
    template_name = 'tasks/task_detail.html'