from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    UserCreateView, TaskListCreateView,TaskDetailView,
    UserTaskListView, TaskCompleteView, TaskByStatusListView
)

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('user-tasks/', UserTaskListView.as_view(), name='user-task-list'),
    path('tasks/<int:pk>/complete/', TaskCompleteView.as_view(), name='task-complete'),
    path('tasks/status/<str:status>/', TaskByStatusListView.as_view(), name='tasks-by-status'),
]
