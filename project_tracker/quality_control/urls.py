from django.urls import path
from quality_control import views
from quality_control.views import bug_detail, feature_detail

app_name = 'quality_control'


urlpatterns = [
    path('', views.index, name='index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),
    path('bugs/<int:bug_id>/', bug_detail, name='bug_detail'),  # Маршрут для получения деталей конкретного бага
    path('features/<int:feature_id>/', feature_detail, name='feature_detail'),  # Маршрут для получения деталей конкретного улучшения
    path('bugs/create/', views.bug_report_create, name='bug_report_create'),
    path('features/create/', views.feature_request_create, name='feature_request_create'),
]