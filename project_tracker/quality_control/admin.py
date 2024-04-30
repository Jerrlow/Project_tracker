from django.contrib import admin
from django.contrib import messages
from .models import BugReport, FeatureRequest

def change_bug_status(modeladmin, request, queryset):
    for bug_report in queryset:
        bug_report.status = 'Resolved'
        bug_report.save()
    modeladmin.message_user(request, f"{queryset.count()} баг(а) были помечены как 'Resolved'.")
change_bug_status.short_description = "Изменить статус выбранных багов на 'Resolved'"

@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    fieldsets = [
        ('Bug Details', {'fields': ['title', 'description', 'project', 'task']}),
        ('Status and Priority', {'fields': ['status', 'priority']}),

    ]
    raw_id_fields = ('project',)
    actions = [change_bug_status]

@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    fieldsets = [
        ('Bug Details', {'fields': ['title', 'description', 'project', 'task']}),
        ('Status and Priority', {'fields': ['status', 'priority']}),
    ]
    raw_id_fields = ('project',)

