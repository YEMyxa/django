from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [

    # path('', views.index),
    # path('projects/', views.project_list, name='project_list'),

    path('', views.IndexView.as_view(), name='index'),
    path('projects/', views.ProjectListView.as_view(), name='project_list'),
    path('projects/<int:project_id>/', views.ProjectDetailView.as_view(), name='project_detail'),
    path('projects/<int:project_id>/tasks/<int:task_id>/', views.TaskDetailView.as_view(), name='task_detail'),
]