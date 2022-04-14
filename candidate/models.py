from django.db import models

class Designation(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name}"
    
class candidate(models.Model):
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
    def __str__(self):
        return f"{self.username}"




