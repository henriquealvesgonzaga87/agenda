from django.db import models
from .models_user import User


class Tasks(models.Model):
    title = models.CharField(max_length=30)
    tags = models.CharField(max_length=30)
    description = models.TextField()
    task_date = models.DateField()
    date_creation_task = models.DateField(auto_now_add=True)
    date_update_task = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tasks'

    def __str__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def get_input_date(self):
        return self.birth_date.strftime("%Y-%m-%dT%H:%M")