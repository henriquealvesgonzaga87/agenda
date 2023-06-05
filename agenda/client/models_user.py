from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    email = models.EmailField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=128, editable=False)

    class Meta:
        db_table = "user"

    def __str__(self):
        return f"{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_input_date(self):
        return self.birth_date.strftime("%Y-%m-%dT%H:%M")
