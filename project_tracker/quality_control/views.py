from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.shortcuts import get_object_or_404
from django.views.generic.base import View
from django.shortcuts import render



# def index(request):
#     bug_list_url = reverse('quality_control:bug_list')
#     feature_list_url = reverse('quality_control:feature_list')
#     return HttpResponse(f"""
#         <h1>Система контроля качества</h1>
#         <a href="{bug_list_url}">Список всех багов</a>
#         <a href="{feature_list_url}">Запросы на улучшение</a>
#     """)

def index(request):
    return render(request, 'quality_control/index.html')


# def bug_list(request):
#     bugs = BugReport.objects.all()
#     bugs_html = "<h1>Список отчетов об ошибках</h1><ul>"
#     for bug in bugs:
#         bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a></li>'
#     bugs_html += '</ul>'
#     return HttpResponse(bugs_html)


def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bugs': bugs})


# def feature_list(request):
#     feature_requests = FeatureRequest.objects.all()
#     feature_requests_html = "<h1>Список запросов на улучшение</h1><ul>"
#     for feature_request in feature_requests:
#         feature_requests_html += f'<li><a href="{feature_request.id}/">{feature_request.title}</a></li>'
#     feature_requests_html += '</ul>'
#     return HttpResponse(feature_requests_html)

def feature_list(request):
    feature_requests = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'features': feature_requests})

# def bug_detail(request, bug_id):
#     bug = get_object_or_404(BugReport, id=bug_id)
#
#     project_url = reverse('tasks:project_detail', args=[bug.project.id])
#     task_url = reverse('tasks:task_detail', args=[bug.project.id, bug.task.id])
#
#     response_html = f"<h1>Детали бага {bug.title}</h1>"
#     response_html += f"<p>Статус бага: <span style='color: red;'>{bug.status}</span></p>"
#     response_html += f"<p>Дата возникновения бага: <span style='color: red;'>{bug.created_at}</span></p>"
#     response_html += f"<p><strong>Подробнее:</strong></p>"
#
#     response_html += f"<p>Проект: <a href='{project_url}'>{bug.project.name}</a></p>"
#     response_html += f"<p>Описание проекта: {bug.project.description}</p>"
#     response_html += f"<p>Задача: <a href='{task_url}'>{bug.task.name}</a></p>"
#     response_html += f"<p>Описание задачи: {bug.task.description}</p>"
#     response_html += f"<p>Статус задачи: {bug.task.status}</p>"
#
#     return HttpResponse(response_html)

def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)

    project_url = reverse('tasks:project_detail', args=[bug.project.id])
    task_url = reverse('tasks:task_detail', args=[bug.project.id, bug.task.id])

    context = {
        'bug': bug,
        'project_url': project_url,
        'task_url': task_url,
    }

    return render(request, 'quality_control/bug_detail.html', context)

# def feature_detail(request, feature_id):
#     feature_request = get_object_or_404(FeatureRequest, id=feature_id)
#     project_url = reverse('tasks:project_detail', args=[feature_request.project.id])
#     task_url = reverse('tasks:task_detail', args=[feature_request.project.id, feature_request.task.id])
#     response_html = f"<h1>Детали улучшения {feature_request.title}</h1>"
#     response_html += f"<p>Статус: <span style='color: red;'>{feature_request.status}</span></p>"
#     response_html += f"<p>Приоритет: <span style='color: red;'>{feature_request.priority}</span></p>"
#     response_html += f"<p><strong>Подробнее:</strong></p>"
#     response_html += f"<p>Проект: <a href='{project_url}'>{feature_request.project.name}</a></p>"
#     response_html += f"<p>Описание проекта: {feature_request.project.description}</p>"
#     response_html += f"<p>Задача: <a href='{task_url}'>{feature_request.task.name}</a></p>"
#     response_html += f"<p>Описание задачи: {feature_request.task.description}</p>"
#     response_html += f"<p>Статус задачи: {feature_request.task.status}</p>"
#
#     return HttpResponse(response_html)

def feature_detail(request, feature_id):
    feature_request = get_object_or_404(FeatureRequest, id=feature_id)
    project_url = reverse('tasks:project_detail', args=[feature_request.project.id])
    task_url = reverse('tasks:task_detail', args=[feature_request.project.id, feature_request.task.id])

    context = {
        'feature_request': feature_request,
        'project_url': project_url,
        'task_url': task_url,
    }

    return render(request, 'quality_control/feature_detail.html', context)


