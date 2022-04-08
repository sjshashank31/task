from django.contrib import admin
from django.urls import path, include
from . import views


app_name = 'tasks'
urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('create-task/', views.create_task, name='create-task'),
    path('tasks/', views.get_tasks, name='tasks'),
    path('task-details/<pk>/', views.task_detail, name='task-details'),
    path('edit-task/<pk>/', views.edit_task, name='edit-task'),
    path('delete-task/<pk>/', views.delete_task, name='delete-task'),
    path('assign-task/<pk>/', views.assign_task, name='assign-task'),
    path('change-status/<pk>/', views.change_status, name='change-status'),
]
