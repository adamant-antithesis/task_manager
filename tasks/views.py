from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Task
from .serializers import UserSerializer, TaskSerializer
from .permissions import IsOwnerOrReadOnly, IsOwnerOrReadOnlyTask


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        # Получаем текущего пользователя, делающего запрос
        user = self.request.user
        serializer.save(user=user)


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]


class UserTaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCompleteView(APIView):
    permission_classes = [IsOwnerOrReadOnlyTask]  # Добавляем кастомный разрешающий класс

    def put(self, request, pk):
        task = Task.objects.get(pk=pk)

        # Проверяем, что текущий пользователь является владельцем задачи
        if task.user != request.user:
            return Response({'error': 'You do not have permission to complete this task.'},
                            status=status.HTTP_403_FORBIDDEN)

        task.status = 'Completed'
        task.save()
        return Response({'status': 'completed'}, status=status.HTTP_200_OK)


class TaskByStatusListView(generics.ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        status = self.kwargs['status']
        return Task.objects.filter(status=status)
