from django.http import HttpResponse
from .models import BugReport, FeatureRequest

from django.shortcuts import render

def index(request):
    return render(request, template_name='quality_control/index.html')

def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bugs': bugs})

def feature_list(request):
    features = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'features': features})

def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")

def feature_id_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")

from django.shortcuts import redirect, get_object_or_404

from .forms import BugReportForm

def add_bug(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            bugreport = form.save(commit=False)
            bugreport.save()
            return redirect('quality_control:bug_list')
    else:
        form = BugReportForm
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

from .forms import FeatureRequestForm

def add_feature(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            featurerequest = form.save(commit=False)
            featurerequest.save()
            return redirect('quality_control:feature_list')
    else:
        form = FeatureRequestForm
    return render(request, 'quality_control/feature_request_form.html', {'form': form})

from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'quality_control/index.html')

from django.views.generic import DetailView

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    template_name = 'quality_control/bug_detail.html'

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    template_name = 'quality_control/feature_detail.html'