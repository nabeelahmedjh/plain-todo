from . import views
from django.urls import path


urlpatterns = [
    path('tasks/', views.TasksView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', views.EditTask.as_view(), name='edit-task'),
    path('tasks/delete/<int:pk>/', views.deleteTask, name='delete-task')
]