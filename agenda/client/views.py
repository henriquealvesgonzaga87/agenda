from urllib import request
from django.shortcuts import redirect
from django.views.generic import CreateView
from .forms_user import UserForm
from .forms_tasks import TaskForm
from .model_tasks import Tasks
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .models_user import UserProfile
from django.contrib import messages


class UserCreateView(CreateView):
    template_name = "client/user.html"
    form_class = UserForm
    success_url = reverse_lazy("tasks:user-create")

    def form_valid(self, form):

        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        birth_date = form.cleaned_data['birth_date']
        email = form.cleaned_data['email']
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']

        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        UserProfile.objects.create(user=user, first_name=first_name, last_name=last_name, birth_date=birth_date,
                                   email=email)

        return redirect("index")


class TaskCreateView(CreateView):
    template_name = "client/task.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks:task-create")

    def form_valid(self, form):
        try:
            task = form.save(commit=False)
            task.user_id = User.objects.get(id=self.request.user.id)
        except Exception:
            messages.error("Error to save your task.")
            print(Exception)
        else:
            task.save()
        return redirect("index")


