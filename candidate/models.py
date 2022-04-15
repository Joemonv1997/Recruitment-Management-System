from django.db import models
from django.contrib.auth.models import User,Group
from django.core.validators import MaxValueValidator, MinValueValidator

class Designation(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
    
class candidate(models.Model):
    inchoices=(('FN','FN'),('AN','AN'),('EN','EN'))
    username=models.CharField(max_length=100,unique=True,blank=True,null=True)
    FullName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Address=models.TextField()
    Designation=models.ForeignKey(Designation,on_delete=models.CASCADE)
    Experience=models.FloatField()
    Programming=models.CharField(max_length=100)
    District=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    Country=models.CharField(max_length=100)
    Interviewer=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    InterviewDate=models.DateField(null=True,blank=True)
    InterviewT=models.CharField(max_length=20,choices=inchoices,null=True,blank=True)
    def __str__(self):
        return f"{self.username}"


class Aptitude(models.Model):
    Name=models.ForeignKey(candidate, on_delete=models.CASCADE)
    aptitude_marks=models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    Remarks=models.TextField(max_length=100)

class FaceToFace(models.Model):
    Name=models.ForeignKey(candidate, on_delete=models.CASCADE)
    personality_marks=models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    communication_marks=models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    technical_marks=models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    logical_marks=models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    average_marks=models.FloatField()
    Remarks=models.TextField(max_length=100)

class MachineMark(models.Model):
    Name=models.ForeignKey(candidate, on_delete=models.CASCADE)
    logic_marks=models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    problemsolve_marks=models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    Finalout_marks=models.FloatField(default=0,validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    average_marks=models.FloatField()
    Remarks=models.TextField(max_length=100)


class CandidateStatus(models.Model):
    status_choices=(("PASSED","PASSED"),("ONHOLD","ONHOLD"),("FAIL","FAIL"))
    Name=models.ForeignKey(candidate, on_delete=models.CASCADE)
    interview_status=models.CharField(max_length=20,choices=status_choices)

