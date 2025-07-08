from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    
    class Types(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        USER = "USER", "User"

    email = models.EmailField(null=False, unique=True)
    username = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=20, choices = Types.choices, default=Types.USER)

    def __str__(self):
        return self.username
    

class Question(models.Model):
    question = models.TextField(null=False)
    answer = models.TextField(null=False)

class Quiz(models.Model):
    questions = models.