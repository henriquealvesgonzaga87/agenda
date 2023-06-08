from django import forms
from .model_tasks import Tasks


class DateTimeInput(forms.DateTimeInput):
    input_type = "date-time"


class TaskForm(forms.ModelForm):
    title = forms.CharField()
    tags = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    task_date = forms.DateTimeField(widget=DateTimeInput())

    class Meta:
        model = Tasks
        fields = (
            "title",
            "tags",
            "description",
            "task_date",
        )
