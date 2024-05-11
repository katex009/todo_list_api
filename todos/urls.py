from django.urls import path 
from .views import TaskDetail, TaskList

urlpatterns = [
    path('', TaskList.as_view(), name='task_list'),
    path('<int:pk>/', TaskDetail.as_view(), name='task_detail'),
]