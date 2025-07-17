from rest_framework import serializers
from .models import User, Quiz, Question

MULTIPLE_CHOICE = 1
TRUE_OR_FALSE = 2
DROPDOWN = 3 
NUMERICAL = 4
TYPE_CHOICES = ((MULTIPLE_CHOICE, 'multiple_choice'), (TRUE_OR_FALSE, 'true_or_false'), (DROPDOWN, 'dropdown'), (NUMERICAL, 'numerical'))

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['id', 'username', 'email', 'role', 'password']

class QuizSerializer(serializers.ModelSerializer):
	#creator = UserSerializer(read_only=True)
	class Meta:
		model = Quiz
		fields = ['title', 'creator', 'types']

	def validate_types(self,value):
		valid_choices = [1,2,3,4]
		if not isinstance(value, list):   #checks value to see if its a list
			raise serializers.ValidationError("Expected 'status' to be a list.") 
		if not set(value).issubset(valid_choices):    #checks to see if things inside value is included in valid_choices
			raise serializers.ValidationError("Invalid choice in 'status'.")
		results = []
		for n in value:
			results.append(TYPE_CHOICES[n-1][1])   #TYPE_CHOICES[n-1][1] gets the string of the tuple in the TYPE_CHOICES
		return results
		
class QuestionSerializer(serializers.ModelSerializer):
	quiz = serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all())
	class Meta:
		model = Question
		fields = ['question', 'answer', 'incorrect', 'quiz']