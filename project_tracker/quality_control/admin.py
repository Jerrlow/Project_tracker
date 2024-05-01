from django.contrib import admin
from django.contrib import messages
from .models import BugReport, FeatureRequest



@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    #STATUS_CHOICES = [('New', 'Новая'), ('In_progress', 'В работе'), ('Completed', 'Завершена')]
    # Отображение в списке
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')

    # Форма редактирования
    fieldsets = [
        ('Bug Details', {'fields': ['title', 'description', 'project', 'task']}),
        ('Status and Priority', {'fields': ['status', 'priority']}),

    ]
    raw_id_fields = ('project',)

    def mark_as_new(self, request, queryset):
        updated = queryset.update(status='New')
        self.message_user(request, f'{updated} отчет(ов) об ошибках помечен(ы) как "Новая".')

    mark_as_new.short_description = 'Пометить как "Новая"'

    def mark_as_in_progress(self, request, queryset):
        updated = queryset.update(status='In_progress')
        self.message_user(request, f'{updated} отчет(ов) об ошибках помечен(ы) как "В работе".')

    mark_as_in_progress.short_description = 'Пометить как "В работе"'

    def mark_as_completed(self, request, queryset):
        updated = queryset.update(status='Completed')
        self.message_user(request, f'{updated} отчет(ов) об ошибках помечен(ы) как "Завершено".')
    mark_as_completed.short_description = 'Пометить как "Завершено"'

    actions = ['mark_as_new', 'mark_as_in_progress', 'mark_as_completed']


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):

    #STATUS_CHOICES = (('pending', 'Рассмотрение'), ('approved', 'Принято'), ('rejected', 'Отклонено'),)
    list_display = ('title', 'project', 'task', 'status', 'priority', 'created_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')


    fieldsets = [
        ('Bug Details', {'fields': ['title', 'description', 'project', 'task']}),
        ('Status and Priority', {'fields': ['status', 'priority']}),
    ]
    raw_id_fields = ('project',)

    def change_request_status_accepted(self, request, queryset):
        updated = queryset.update(status='approved')
        self.message_user(request, f'{updated} запрос(ов) помечен(ы) как "Принято".')

    change_request_status_accepted.short_description = 'Пометить как "Принято"'

    def change_request_status_in_review(self, request, queryset):
        updated = queryset.update(status='pending')
        self.message_user(request, f'{updated} запрос(ов) помечен(ы) как "В рассмотрении".')

    change_request_status_in_review.short_description = 'Пометить как "В рассмотрении"'

    def change_request_status_rejected(self, request, queryset):
        updated = queryset.update(status='rejected')
        self.message_user(request, f'{updated} запрос(ов) помечен(ы) как "Отклонено".')

    change_request_status_rejected.short_description = 'Пометить как "Отклонено"'

    actions = ['change_request_status_accepted', 'change_request_status_in_review', 'change_request_status_rejected']
