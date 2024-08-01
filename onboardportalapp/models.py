from django.db import models
import datetime
# Create your models here.


class User(models.Model):
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)


class Branch(models.Model):
    branch_name=models.CharField(max_length=20)

class Course(models.Model):
    course_name=models.CharField(max_length=20)
    course_duration=models.IntegerField(default=1)
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE,default=1)




class Staff(models.Model):
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    status=models.BooleanField()
    staff_name=models.CharField(max_length=20)
    experience=models.IntegerField()
    subject=models.CharField(max_length=20)
    course=models.ManyToManyField(Course)


class Student(models.Model):
    branch=models.ForeignKey(Branch,on_delete=models.CASCADE)
    status=models.BooleanField()
    student_name=models.CharField(max_length=20)
    course=models.ManyToManyField(Course)
    start_Date=models.DateField(default=datetime.date.today)
    end_Date=models.DateField(default=datetime.date.today)


      
