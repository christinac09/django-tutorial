from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .models import User, Question, Quiz
from .serializers import UserSerializer, QuestionSerializer, QuizSerializer
from rest_framework.response import Response


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

""" class QuizViewSet(APIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    
    def post(self,request): 
        print(request.data)
        creator = User.objects.get(id=request.data['creator_id'])
        quiz = Quiz.objects.create(creator=creator, title=request.data['title'], uuid_id=request.data['uuid_id'])
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)
 """  #dunno what this is

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
