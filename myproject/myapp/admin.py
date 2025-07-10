from django.contrib import admin

# Register your models here.
from .models import User, Role, Type, Quiz, Question

admin.site.register(User, Role, Type, Quiz, Question)