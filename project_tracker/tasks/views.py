from django.urls import reverse
from django.http import HttpResponse
from .models import Project, Task


def index(request):
    project_list_url = reverse('tasks:project_list')  # URL для "Список всех проектов"
    quality_control_url = reverse('quality_control:index')  # URL для "Перейти в систему контроля качества"

    link_html = f'<a href="{project_list_url}">Список всех проектов</a> | <a href="{quality_control_url}">Перейти в систему контроля качества</a>'

    return HttpResponse(f'<h1>Главная страница приложения Tasks</h1><p>{link_html}</p>')


def project_list(request):
    projects = Project.objects.all()
    projects_html = '<h1>Список всех проектов</h1><ul>'
    for project in projects:
        projects_html += f"<li>{project.name}</li>"
    projects_html += "</ul>"
    return HttpResponse(projects_html)
