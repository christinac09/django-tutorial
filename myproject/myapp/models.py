from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.contrib.postgres.fields import ArrayField
import uuid

class User(AbstractUser):
    USER = 1
    SUPERVISOR = 2
    ROLE_CHOICES = ((USER, "user"), (SUPERVISOR, 'supervisor'))

    role = models.CharField(choices=ROLE_CHOICES, null=False, default=(USER, 'user'))
    email = models.EmailField(null=False, unique=True)
    username = models.CharField(max_length=255, null=False, unique=True)
    #password = models.CharField(max_length=255, null=False)  included in abstractuser(?)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username',]

    def __str__(self):
        return "{}".format(self.email)


""" class Type(models.Model):
    MULTIPLE_CHOICE = 1
    TRUE_OR_FALSE = 2
    DROPDOWN = 3 
    NUMERICAL = 4
    TYPE_CHOICES = ((MULTIPLE_CHOICE, 'multiple_choice'), (TRUE_OR_FALSE, 'true_or_false'), (DROPDOWN, 'dropdown'), (NUMERICAL, 'numerical'))

    id = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, primary_key=True)
    
    def __str__(self):
        return self.get_id_display() """
    
class Quiz(models.Model):
    title = models.CharField(max_length=255, null=False)
    types = models.JSONField(null=True)
    creator = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)

class Question(models.Model):
    question = models.CharField(max_length=255, null=False)
    answer = models.JSONField(default=list)
    incorrect = models.JSONField(default=list, blank=True, null=True)   
    quiz = models.ForeignKey(Quiz, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)