task_manager
TodoApp with JWT

Project "Task Manager" using Django REST Framework
The "Task Manager" project is a simple web application for task management, built using Django REST Framework (DRF) to create the API. This application allows users to create, view, update, and delete tasks. User authentication is implemented using JWT (JSON Web Token).

                                                     IMPORTANT!
The project can be deployed in a Docker container or run on a local server.

1)Deployment using Docker:

1.Clone the repository:

  git clone https://github.com/adamant-antithesis/task_manager.git

2.Navigate to the task_manager directory (at the same level as the manage.py file):

  cd task_manager

3.Create and launch the containers using the following command:

  docker-compose up --build

4.Use Postman to access the API endpoints.

2)Local Server Setup:

Requirements

  Python 3.x
  Django 3.x
  Django REST Framework (DRF)
  djangorestframework-simplejwt
  Installation and Configuration

1.Clone the repository:

  git clone https://github.com/adamant-antithesis/task_manager.git

2.Navigate to the task_manager directory (at the same level as the manage.py file):

  cd task_manager

3.Install dependencies:

  pip install -r requirements.txt

4.Create a database with the name "todobase":

Access the PostgreSQL shell by using the following command and press Enter:

  psql -U <username> (use the default username - postgres, password - postgres)

Once you are in the PostgreSQL shell, create the database "todobase" with the following command:

  CREATE DATABASE todobase;

5.Exit the PostgreSQL shell:

To exit the PostgreSQL shell, type the command \q and press Enter.

6.Create and apply migrations (you should be in the task_manager directory at the same level as the manage.py file):

  python manage.py makemigrations
  python manage.py migrate

7.Create a superuser to manage the admin panel:

  python manage.py createsuperuser

8.Run tests:

  python manage.py test tasks

9.Start the server:

  python manage.py runserver

10.Use Postman to access the API endpoints.


                                                 API ENDPOINTS
             
1.Access to Django admin panel.

----GET /admin/

Full URL: http://127.0.0.1:8000/admin/
Description: Django administrative interface. In the browser, navigate to the provided URL and authenticate using the superuser credentials.
Function: Allows the administrator to manage data in the admin panel.

2.User Model

----POST /api/users/

Full URL: http://127.0.0.1:8000/api/users/
Description: Create a new user.
Function: Registers a new user in the system. (username and email fields must be unique)

Data to be sent:

{
"username": "username",
"first_name": "first_name",
"last_name": "last_name",
"email": "email",
"password": "password"
}

3.Authentication

----POST /api/token/

Full URL: http://127.0.0.1:8000/api/token/
Description: Obtain an access token.
Function: Authenticates the user and issues an access token to access protected endpoints.

Data to be sent:

{
"username": "username",
"password": "password"
}

----POST /api/token/refresh/

Full URL: http://127.0.0.1:8000/api/token/refresh/
Description: Refresh an access token.
Function: Refreshes and provides a new access token based on the previous one.
The refresh token is obtained by an authenticated user along with the access token at http://127.0.0.1:8000/api/token/

Data to be sent:

{
"refresh": "refresh (obtained from the response of POST /api/token/)"
}

4.Task Model

----GET /api/tasks/

Full URL: http://127.0.0.1:8000/api/tasks/
Description: Get a list of tasks.
Function: Retrieves a list of all tasks.

Data to be sent:

No data required. Authentication required with the token - Authorization - Bearer Token - {access_token}

----POST /api/tasks/

Full URL: http://127.0.0.1:8000/api/tasks/
Description: Create a new task. Authentication required with the token - Authorization - Bearer Token - {access_token}
Function: Allows creating a new task associated with the current user.

Data to be sent:

{
"title": "title",
"description": "description",
"status": "status (Options: New, In Progress, Completed)",
}

----GET /api/tasks/int:pk/

Full URL: http://127.0.0.1:8000/api/tasks/int:pk/
Description: Get task details by identifier.
Function: Returns details of a specific task based on its unique identifier (pk).

Data to be sent:

No data required. Authentication required with the token - Authorization - Bearer Token - {access_token}

----PUT /api/tasks/int:pk/

Full URL: http://127.0.0.1:8000/api/tasks/int:pk/
Description: Update a task. Only the task's author can perform updates.
Function: Allows updating information about an existing task.

Data to be sent:

{
"title": "title",
"description": "description",
"status": "status (Options: New, In Progress, Completed)",
}

----PATCH /api/tasks/int:pk/

Full URL: http://127.0.0.1:8000/api/tasks/int:pk/
Description: Partially update a task. Only the task's author can perform updates.
Function: Allows partially updating information about an existing task.

Data to be sent (any or multiple fields):

{
"title": "title",
"description": "description",
"status": "status (Options: New, In Progress, Completed)"
}

----DELETE /api/tasks/int:pk/

Full URL: http://127.0.0.1:8000/api/tasks/int:pk/
Description: Delete a task. Only the task's author can perform deletion.
Function: Allows deleting a task based on its unique identifier.

Data to be sent:

No data required. Authentication required with the token - Authorization - Bearer Token - {access_token}

----GET /api/user-tasks/

Full URL: http://127.0.0.1:8000/api/user-tasks/
Description: Get a list of tasks for the current user.
Function: Returns a list of tasks associated with the currently authenticated user.

Data to be sent:

No data required. Authentication required with the token - Authorization - Bearer Token - {access_token}

----PUT /api/tasks/int:pk/complete/

Full URL: http://127.0.0.1:8000/api/tasks/int:pk/complete/
Description: Mark a task as completed.
Function: Changes the status of a task to "Completed".

No data required. Authentication required with the token - Authorization - Bearer Token - {access_token}

----GET /api/tasks/status/str:status/

Full URL: http://127.0.0.1:8000/api/tasks/status/str:status/
Description: Get a list of tasks by status.
Function: Returns a list of tasks with the specified status.

No data required. Authentication required with the token - Authorization - Bearer Token - {access_token}

Status options in the URL: new, in_progress, completed
