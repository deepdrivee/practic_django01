from django.db import models

# Create your models here.
class student(models.Model):
    studentid =models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    type = [("male","male"),("female","female")]
    gender = models.CharField(max_length=50,choices=type,default=None)
    photo = models.ImageField(upload_to="studentImg")