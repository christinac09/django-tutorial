from django.urls import path
from . import views

urlpatterns = [
    path('questions/', views.questions, name='questions'),
]

# 'questions/' = url
# view.questions = name of views from views.py
# name doesn't matter