from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_list, name="tasks"),
    path('download/', views.download_tasks, name="download_tasks"),
    path('add/', views.add_task, name="add_task"),
    path('edit/<int:id>/', views.edit_task, name="edit_task"),
    path('delete/<int:id>/', views.delete_task, name="delete_task"),
]
