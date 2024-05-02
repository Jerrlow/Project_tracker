from django import forms
from .models import BugReport, Project, Task

class BugReportForm(forms.ModelForm):
    class Meta:
        model = BugReport
        fields = ['title', 'description', 'status', 'priority', 'project', 'task']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.all()
        self.fields['task'].queryset = Task.objects.all()


from django import forms
from .models import FeatureRequest

class FeatureRequestForm(forms.ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'status', 'priority', 'project', 'task']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.all()
        self.fields['task'].queryset = Task.objects.all()