from django.db import models


import uuid
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='doctors')
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='doctors/', blank=True, null=True)
    def __str__(self):
        return self.name