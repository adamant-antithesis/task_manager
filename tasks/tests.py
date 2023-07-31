from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthenticationTests(APITestCase):

    def setUp(self):
        # Создаем пользователя
        self.user = User.objects.create_user(username='test', password='testpassword')
        # Вызываем метод базового класса setUp
        super().setUp()

    # POST /api/token/
    def test_get_access_token(self):
        url = reverse('token_obtain_pair')
        data = {'username': 'test', 'password': 'testpassword'}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

        self.access_token = response.data['access']
        token = response.data['access']
        return token

    # POST /api/users/
    def test_create_user(self):
        self.test_get_access_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        url = reverse('user-create')
        data = {
            "username": "test_antithesis",
            "first_name": "antithesis",
            "email": "antithesis@gmail.com",
            "password": "252712"
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertIn('first_name', response.data)
        self.assertIn('email', response.data)

    # GET /api/tasks/
    def test_get_task_list(self):
        self.test_get_access_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        url = reverse('task-list-create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('results', response.data)
        tasks = response.data['results']
        self.assertEqual(len(tasks), 0)

    # POST /api/tasks/
    def test_create_task(self):
        self.test_get_access_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        url = reverse('task-list-create')
        data = {
            "title": "antithesis",
            "status": "New",
            "user": self.user.id
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data['title'], "antithesis")
        self.assertEqual(response.data['status'], "New")
        self.assertEqual(response.data['user'], self.user.id)

    # GET /api/tasks/{task_id}/
    def test_get_task_detail(self):
        self.test_get_access_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        url = reverse('task-list-create')
        data = {
            "title": "antithesis",
            "status": "New",
            "user": self.user.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task_id = response.data['id']

        url = reverse('task-detail', kwargs={'pk': task_id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], task_id)
        self.assertEqual(response.data['title'], 'antithesis')
        self.assertEqual(response.data['description'], '')
        self.assertEqual(response.data['status'], 'New')
        self.assertEqual(response.data['user'], self.user.id)

    # PUT /api/tasks/{task_id}/
    def test_update_task(self):
        self.test_get_access_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        url = reverse('task-list-create')
        data = {
            "title": "antithesis",
            "status": "New",
            "user": self.user.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        task_id = response.data['id']

        url = reverse('task-detail', kwargs={'pk': task_id})
        data = {
            "title": "updated_task",
            "status": "Completed",
            "user": self.user.id
        }
        response = self.client.put(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], task_id)
        self.assertEqual(response.data['title'], 'updated_task')
        self.assertEqual(response.data['description'], '')
        self.assertEqual(response.data['status'], 'Completed')
        self.assertEqual(response.data['user'], self.user.id)

    # PATCH /api/tasks /{task_id}/
    def test_partial_update_task(self):
        self.test_get_access_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Создаем задачу с идентификатором 1
        url = reverse('task-list-create')
        data = {
            "title": "antithesis",
            "status": "New",
            "user": self.user.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Получаем идентификатор созданной задачи
        task_id = response.data['id']

        url = reverse('task-detail', kwargs={'pk': task_id})
        data = {
            "status": "Completed"
        }
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], task_id)
        self.assertEqual(response.data['title'], 'antithesis')  # Не должно измениться
        self.assertEqual(response.data['description'], '')  # Не должно измениться
        self.assertEqual(response.data['status'], 'Completed')  # Обновленное значение
        self.assertEqual(response.data['user'], self.user.id)

    # DELETE /api/tasks/{task_id}/
    def test_delete_task(self):
        self.test_get_access_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Создаем задачу с идентификатором 1
        url = reverse('task-list-create')
        data = {
            "title": "antithesis",
            "status": "New",
            "user": self.user.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Получаем идентификатор созданной задачи
        task_id = response.data['id']

        url = reverse('task-detail', kwargs={'pk': task_id})
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Отправляем GET-запрос для проверки, что задачи больше нет в списке
        url = reverse('task-list-create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что в ответе список задач пуст
        tasks = response.data['results']
        self.assertEqual(len(tasks), 0)

    # PUT /api/tasks/{task_id}/complete/
    def test_complete_task(self):
        self.test_get_access_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        # Создаем задачу с идентификатором 1
        url = reverse('task-list-create')
        data = {
            "title": "antithesis",
            "status": "New",
            "user": self.user.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Получаем идентификатор созданной задачи
        task_id = response.data['id']

        url = reverse('task-complete', kwargs={'pk': task_id})
        response = self.client.put(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что в ответе задача теперь имеет статус "Completed"
        self.assertEqual(response.data['status'], "completed")

        # Отправляем GET-запрос для получения задачи по id
        url = reverse('task-detail', kwargs={'pk': task_id})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что в ответе задача также имеет статус "Completed"
        self.assertEqual(response.data['status'], "Completed")

    # GET /api/tasks/status/{status}
    def test_get_tasks_by_status(self):
        self.test_get_access_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        tasks_data = [
            {"title": "Task 1", "status": "New", "user": self.user.id},
            {"title": "Task 2", "status": "Completed", "user": self.user.id},
            {"title": "Task 3", "status": "Completed", "user": self.user.id},
            {"title": "Task 4", "status": "New", "user": self.user.id},
        ]
        for task_data in tasks_data:
            url = reverse('task-list-create')
            response = self.client.post(url, task_data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Отправляем GET-запрос для получения задач со статусом "New"
        url = reverse('tasks-by-status', kwargs={'status': 'New'})
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что в ответе присутствует список задач (количество задач со статусом "New" - 2)
        self.assertIn('results', response.data)
        tasks = response.data['results']
        self.assertEqual(len(tasks), 2)

        # Проверяем, что задачи в списке имеют статус "New"
        task = tasks[0]
        self.assertEqual(task['status'], 'New')
