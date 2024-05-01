from django.http import HttpResponse

from django.http import HttpResponse
from django.urls import reverse
from .models import BugReport, FeatureRequest
from django.shortcuts import get_object_or_404



def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')
    return HttpResponse(f"""
        <h1>Система контроля качества</h1>
        <a href="{bug_list_url}">Список всех багов</a>
        <a href="{feature_list_url}">Запросы на улучшение</a>
    """)


def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = "<h1>Список отчетов об ошибках</h1><ul>"
    for bug in bugs:
        bugs_html += f'<li><a href="{bug.id}/">{bug.title}</a></li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)


def feature_list(request):
    return HttpResponse("<h1>Список запросов на улучшение</h1>")


def bug_detail(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)

    project_url = reverse('tasks:project_detail', args=[bug.project.id])
    task_url = reverse('tasks:task_detail', args=[bug.project.id, bug.task.id])

    response_html = f"<h1>Детали бага {bug.title}</h1>"
    response_html += f"<p>Статус бага: <span style='color: red;'>{bug.status}</span></p>"
    response_html += f"<p>Дата возникновения бага: <span style='color: red;'>{bug.created_at}</span></p>"
    response_html += f"<p><strong>Подробнее:</strong></p>"

    response_html += f"<p>Проект: <a href='{project_url}'>{bug.project.name}</a></p>"
    response_html += f"<p>Описание проекта: {bug.project.description}</p>"
    response_html += f"<p>Задача: <a href='{task_url}'>{bug.task.name}</a></p>"
    response_html += f"<p>Описание задачи: {bug.task.description}</p>"
    response_html += f"<p>Статус задачи: {bug.task.status}</p>"

    return HttpResponse(response_html)



def feature_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")
