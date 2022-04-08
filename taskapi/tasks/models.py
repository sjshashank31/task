from django.db import models
from django.contrib.auth.models import User
ROLES = (("C", "CLIENT"),
         ("E", "EMPLOYEE"),
         ("M", "MANAGER")
         )


class Role(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=200, choices=ROLES)

    def __str__(self):
        return self.role


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=1080)
    description = models.TextField()
    assigned_to = models.OneToOneField(User, related_name='assigned_to', on_delete=models.SET_NULL, null=True, blank=True)
    task_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


