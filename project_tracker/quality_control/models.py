from django.db import models
from tasks.models import Project, Task


class BugReport(models.Model):
    STATUS_CHOICES = [('New', 'Новая'), ('In_progress', 'В работе'), ('Completed', 'Завершена')]
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='New')
    priority = models.IntegerField(choices=((1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Critical')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class FeatureRequest(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    STATUS_CHOICES = (
        ('pending', 'В рассмотрении'),
        ('approved', 'Принято'),
        ('rejected', 'Отклонено'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.IntegerField(choices=((1, 'Low'), (2, 'Medium'), (3, 'High'), (4, 'Critical')))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title