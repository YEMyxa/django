from django.http import HttpResponse
from django.urls import reverse
from .models import Project, Task

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

from .forms import FeedbackForm
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ProjectForm

def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:project_list')
    else:
        form = ProjectForm
    return render(request, 'tasks/project_create.html', {'form': form})

from .forms import TaskForm

def add_task_to_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.save()
            return redirect('tasks:project_detail', project_id=project.id)
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form, 'project': project})

from django.core.mail import send_mail

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            recipients = ['info@example.com']
            recipients.append(email)

            send_mail(subject, message, email, recipients)

            return redirect('/tasks')
    else:
        form = FeedbackForm()
    return render(request, 'tasks/feedback.html', {'form': form})

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