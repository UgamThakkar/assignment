from typing import Text
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Post(models.Model):
    title = models.CharField(max_length=40)
    user = ForeignKey(User, on_delete=models.CASCADE, null=True)  #represents a single user can do multiple posts or a single user can be associated with multiple posts.
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


