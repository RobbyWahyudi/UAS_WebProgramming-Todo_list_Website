from django.urls import path
from . import views

urlpatterns = [
    path("task/", views.task, name="task"),
    path("create_task/", views.create_task, name="create-task"),
    path("edit_task/<int:task_id>", views.edit_task, name="edit-task"),
    path("complete_task/<int:task_id>/", views.complete_task, name="complete-task"),
    path("delete_task/<int:task_id>/", views.delete_task, name="delete-task"),
    path("add_category/", views.add_category, name="add-category"),
    path("logout/", views.user_logout, name="user-logout"),
]
