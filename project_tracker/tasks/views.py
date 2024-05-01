from django.urls import reverse
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.shortcuts import render

def index(request):
    return render(request, 'tasks/index.html')
# def index(request):
#     template = render_to_string('tasks/index.html')
#     return HttpResponse(template)

# def index(request):
#     projects_list_url = reverse('tasks:projects_list')
#     quality_control_url = reverse('quality_control:index')  # URL для "Перейти в систему контроля качества"
#     link_html = f'<a href="{projects_list_url}">Список всех проектов</a> | <a href="{quality_control_url}">Перейти в систему контроля качества</a>'
#     return HttpResponse(f'<h1>Главная страница приложения Tasks</h1><p>{link_html}</p>')


# def projects_list(request):
#     projects = Project.objects.all()
#     projects_html = '<h1>Список проектов</h1><ul>'
#     for project in projects:
#         projects_html += f'<li><a href="{project.id}/">{project.name}</a></li>'
#     projects_html += '</ul>'
#     return HttpResponse(projects_html)

def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'tasks/projects_list.html', {'project_list': projects})

def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    tasks = project.tasks.all()
    response_html = f'<h1>{project.name}</h1><p>{project.description}</p>'
    response_html += '<h2>Задачи</h2><ul>'
    for task in tasks:
        response_html += f'<li><a href="tasks/{task.id}/">{task.name}</a></li>'
    response_html += '</ul>'
    return HttpResponse(response_html)

def task_detail(request, project_id, task_id):
    project = get_object_or_404(Project, id=project_id)
    task = get_object_or_404(Task, id=task_id, project=project)
    response_html = f'<h1>{task.name}</h1><p>{task.description}</p>'
    return HttpResponse(response_html)