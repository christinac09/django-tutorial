from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
import uuid

class Role(models.Model):
    USER = 1
    ADMIN = 2
    ROLE_CHOICES = ((USER, "user"), (ADMIN, 'admin'))

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class User(AbstractUser):
    role = models.ForeignKey(Role, null=False)
    email = models.EmailField(null=False, unique=True)
    username = models.CharField(max_length=255, null=False, unique=True)
    #password = models.CharField(max_length=255, null=False)  included in abstractuser(?)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username',]

    def __str__(self):
        return "{}".format(self.email)


class Type(models.Model):
    MULTIPLE_CHOICE = 1
    TRUE_OR_FALSE = 2
    DROPDOWN = 3   #fill in the blank with dropdown
    NUMERICAL = 4
    TYPE_CHOICES = ((MULTIPLE_CHOICE, 'multiple_choice'), (TRUE_OR_FALSE, 'true_or_false'), (DROPDOWN, 'dropdown'), (NUMERICAL, 'numerical'))

    id = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, primary_key=True)
    
    def __str__(self):
        return self.get_id_display()
    
class Quiz(models.Model):
    uuid_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, null=False)
    types = models.ManyToManyField(Type, null=False)
    creator = models.ForeignKey(User, null=False)
    
    def __str__(self):
        return self.uuid_id

class Question(models.Model):
    uuid_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.CharField(max_length=255, null=False)
    answer = ArrayField(models.CharField(max_length=255), null=False, blank=False, default=list)
    incorrect = ArrayField(models.CharField(max_length=255), blank=True, default=list)
    quiz = models.ForeignKey(Quiz, null=False)

    def __str__(self):
        return self.uuid_id