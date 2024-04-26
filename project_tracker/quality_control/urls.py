from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [

    # path('', views.index, name='main'),
    # path('bug_detail/<int:bug_id>/', views.bug_detail, name='bug_detail'),
    # path('feature_detail/<int:feature_id>/', views.feature_id_detail, name='feature_detail'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),

    path('', views.IndexView.as_view(), name='index'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
]