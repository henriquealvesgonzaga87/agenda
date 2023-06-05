from django.urls import path
from .views import UserCreateView, TaskCreateView
from django.contrib.auth.decorators import login_required

app_name = "tasks"

urlpatterns = [
    path("user/create/", UserCreateView.as_view(), name="user-create"),
    path("user/<int:user_id>/task/create/", login_required(TaskCreateView.as_view()), name="task-create")
]
