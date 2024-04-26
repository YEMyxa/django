from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest

def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')
    html = (f"<h1>Система контроля качества</h1>"
            f"<a href='{bug_list_url}'>Список всех багов</a><br/>"
            f"<a href='{feature_list_url}'>Запросы на улучшение</a>")
    return HttpResponse(html)

def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список отчетов об ошибках</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a> ({bug.status})</li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)

def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список запросов на улучшение</h1><ul>'
    for feature in features:
        features_html += f'<li><a href="{feature.id}/">{feature.title}</a> ({feature.status})</li>'
    features_html += '</ul>'
    return HttpResponse(features_html)

def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")

def feature_id_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")

from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        bug_list_url = reverse('quality_control:bug_list')
        feature_list_url = reverse('quality_control:feature_list')
        html = (f"<h1>Система контроля качества</h1>"
                f"<a href='{bug_list_url}'>Список всех отчетов об ошибках</a><br/>"
                f"<a href='{feature_list_url}'>Запросы на улучшение</a>")
        return HttpResponse(html)

from django.views.generic import DetailView

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        response_html = (f'<h1>{bug.title}</h1><p>{bug.description}</p>'
                         f'<p>Статус: {bug.status}</br>'
                         f'Приоритет: {bug.priority}</br>'
                         f'Проект->задача: {bug.project}->{bug.task}</p>')
        return HttpResponse(response_html)

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = (f'<h1>{feature.title}</h1><p>{feature.description}</p>'
                         f'<p>Статус: {feature.status}</br>'
                         f'Приоритет: {feature.priority}</br>'
                         f'Проект->задача: {feature.project}->{feature.task}</p>')
        return HttpResponse(response_html)