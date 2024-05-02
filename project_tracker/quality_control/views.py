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



def bug_list(request):
    bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {'bugs': bugs})


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


def feature_list(request):
    feature_requests = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {'features': feature_requests})

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


from django.shortcuts import render, redirect
from .forms import BugReportForm
from .models import BugReport

def bug_report_create(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_list')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})

from .forms import FeatureRequestForm
from .models import FeatureRequest

def feature_request_create(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            feature_request = form.save(commit=False)
            feature_request.save()
            return redirect('quality_control:feature_list')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})



# Обновление бага
def bug_report_update(request, bug_id):
    bug = get_object_or_404(BugReport, id=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('quality_control:bug_detail', bug_id=bug.id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bug_report_form_update.html', {'form': form})

# Удаление бага
def bug_report_delete(request, bug_id):

    # project = get_object_or_404(Project, pk=project_id)
    # project.delete()
    # return redirect('tasks:projects_list')
    bug = get_object_or_404(BugReport, id=bug_id)
    bug.delete()
    return redirect('quality_control:bug_list')


def feature_request_update(request, feature_id):
    feature_request = get_object_or_404(FeatureRequest, id=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature_request)
        if form.is_valid():
            form.save()
            return redirect('quality_control:feature_detail', feature_id=feature_request.id)
    else:
        form = FeatureRequestForm(instance=feature_request)
    return render(request, 'quality_control/feature_request_form_update.html', {'form': form})


def feature_request_delete(request, feature_id):
    feature_request = get_object_or_404(FeatureRequest, id=feature_id)
    feature_request.delete()
    return redirect('quality_control:feature_list')
    # return render(request, 'quality_control/feature_request_form_delete.html', {'feature_request': feature_request})

