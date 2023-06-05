from django import forms
from .model_tasks import Tasks


class DateInput(forms.DateInput):
    input_type = "date"


class TaskForm(forms.ModelForm):
    title = forms.CharField()
    tags = forms.CharField()
    description = forms.CharField()
    task_date = forms.DateField(widget=DateInput())
    active = forms.BooleanField()

    class Meta:
        model = Tasks
        fields = (
            "title",
            "tags",
            "description",
            "task_date",
            "active"
        )
