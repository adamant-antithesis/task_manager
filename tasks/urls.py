from django.urls import re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    UserCreateView, TaskListCreateView, TaskDetailView,
    UserTaskListView, TaskCompleteView, TaskByStatusListView
)

urlpatterns = [
    re_path(r'^users/$', UserCreateView.as_view(), name='user-create'),
    re_path(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    re_path(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
    re_path(r'^tasks/(?P<pk>\d+)/$', TaskDetailView.as_view(), name='task-detail'),
    re_path(r'^tasks/$', TaskListCreateView.as_view(), name='task-list-create'),
    re_path(r'^user-tasks/$', UserTaskListView.as_view(), name='user-task-list'),
    re_path(r'^tasks/(?P<pk>\d+)/complete/$', TaskCompleteView.as_view(), name='task-complete'),
    re_path(r'^tasks/status/(?P<status>[\w-]+)/$', TaskByStatusListView.as_view(), name='tasks-by-status'),
]
