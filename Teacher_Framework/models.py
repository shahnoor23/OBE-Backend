import datetime

from django.db import models
from django.utils import timezone
from Accounts.models import User
from Chairman_Framework.models import CLO


class Assignment(models.Model):
    title = models.CharField(max_length=200, null=True)
    teacher = models.ForeignKey(
        User, related_name="teacher_create", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Question(models.Model):
    question_text = models.CharField(max_length=200, null=True)
    quizz = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True)
    answer =  models.ForeignKey(CLO, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    choice_text = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.choice_text


class GradedAssignment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(
        Assignment, on_delete=models.SET_NULL, blank=True, null=True)
    grade = models.FloatField()

    def __str__(self):
        return self.student.username



#Assign Assignment to Student By Teacher

class Assignment_Assign_To_Student(models.Model):
    student_name = models.ManyToManyField(User)
    assignment = models.ManyToManyField(Assignment)











#----------------------------------GRADED ASSIGNMENT -------------------------------------#

class Graded(models.Model):
    question_text = models.CharField(max_length=200)
    
    def __str__(self):
        return self.question_text
        

class CLO_Graded(models.Model):
    question = models.ForeignKey(Graded, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text





# --------------------------- Testing -------------------------- #

class GA(models.Model):
    tittle = models.CharField(max_length=200)

    def __str__(self):
        return self.tittle
        

class GQ(models.Model):
    question = models.ForeignKey(GA, on_delete=models.CASCADE)
    clo_text = models.CharField(max_length=200)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text