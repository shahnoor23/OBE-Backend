from Chairman_Framework.serializers import CLOSerializer
from rest_framework import serializers
from .models import Choice, Question, Assignment,Assignment_Assign_To_Student, GradedAssignment, Graded, CLO_Graded , GA , GQ
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()
from Chairman_Framework.serializers import CLOSerializer

# read below blog if any confusion
# https://medium.com/@raaj.akshar/creating-reverse-related-objects-with-django-rest-framework-b1952ddff1c

class StringSerializer(serializers.StringRelatedField):
    def to_internal_value(self, value):
        return value


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('choice_text',)


class QuestionSerializer(serializers.ModelSerializer):

    choice_set = ChoiceSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'
        
        
    def create(self, validated_data):
        choice_validated_data = validated_data.pop('choice_set')
        question = Question.objects.create(**validated_data)
        choice_set_serializer = self.fields['choice_set']
        for each in choice_validated_data:
            each['question'] = question
        choices = choice_set_serializer.create(choice_validated_data)
        return question


class AssignmentSerializer(serializers.ModelSerializer):

    question_set = QuestionSerializer(many=True)

    class Meta:
        model = Assignment
        fields = '__all__'

    def create(self, validated_data):
        #print(validated_data)
        question_validated_data = validated_data.pop('question_set')
        quizz = Assignment.objects.create(**validated_data)
      
        question_set_serializer = self.fields['question_set']
        for each in question_validated_data:
            each['quizz'] = quizz
        questions = question_set_serializer.create(question_validated_data)
        return quizz


class GradedAssignmentSerializer(serializers.ModelSerializer):
    student = StringSerializer(many=False)

    class Meta:
        model = GradedAssignment
        fields = ('__all__')




# teacher assign student assignment 
class AssignAssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment_Assign_To_Student
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['assignment'] = AssignmentSerializer(
            read_only=True, many=True)
        return super(AssignAssignmentSerializer, self).to_representation(instance)









#-----------------------------------GRADED ----------------------------------- #
class CLO_GradedSerializer(serializers.ModelSerializer):
    class Meta:
        model = CLO_Graded
        fields = ('choice_text',)

class GradedSerializer(serializers.ModelSerializer):

    choice_set = CLO_GradedSerializer(many=True)
    
    class Meta:
        model = Graded
        fields = '__all__'

    def create(self, validated_data):
        choice_validated_data = validated_data.pop('choice_set')
        question = Graded.objects.create(**validated_data)
        choice_set_serializer = self.fields['choice_set']
        for each in choice_validated_data:
            each['question'] = question
        choices = choice_set_serializer.create(choice_validated_data)
        return question    










#------------------------- TESTING ----------------------------- #

class GQSerializer(serializers.ModelSerializer):
    class Meta:
        model = GQ
        fields = ('clo_text',)

class GASerializer(serializers.ModelSerializer):

    choice_set = GQSerializer(many=True)
    class Meta:
        model = GA
        fields = '__all__'


    def create(self, validated_data):
        choice_validated_data = validated_data.pop('choice_set')
        ga = GA.objects.create(**validated_data)
        choice_set_serializer = self.fields['choice_set']
        for each in choice_validated_data:
            each['ga'] = ga
        choices = choice_set_serializer.create(choice_validated_data)
        return ga     