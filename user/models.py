from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)