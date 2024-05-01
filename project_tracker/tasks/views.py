from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse

def index(request):
    quality_control_url = reverse('quality_control:index')
    link_html = f'<a href="{quality_control_url}">Перейти в систему контроля качества</a>'
    return HttpResponse(f'<h1>Главная страница приложения Tasks</h1><p>{link_html}</p>')