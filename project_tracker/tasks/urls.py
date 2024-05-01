from django.urls import path, include
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index),
    path('quality_control/', include('quality_control.urls'))
]