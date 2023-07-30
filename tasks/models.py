from django.contrib.auth import get_user_model
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True, blank=False)
    first_name = models.CharField(max_length=100)
    last_name = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email


class Task(models.Model):
    STATUS_CHOICES = (
        ('New', 'New'),
        ('Actual', 'Actual'),
        ('Completed', 'Completed'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title
