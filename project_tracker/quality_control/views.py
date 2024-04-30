from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Система контроля качества</h1><a href='/bugs/'>Список всех багов</a> <a href='/features/'>Запросы на улучшение</a>")

def bug_list(request):
    return HttpResponse("<h1>Список отчетов об ошибках</h1>")

def feature_list(request):
    return HttpResponse("<h1>Список запросов на улучшение</h1>")


def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")


def feature_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")

