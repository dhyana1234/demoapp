from django.db import models

# Create your models here.
class Student(models.Model):
    Student_name=models.CharField(max_length=200)
    # Student_no=models.IntegerField
    Student_image=models.ImageField(upload_to="student")
    English=models.TextField(max_length=100)
    Science=models.TextField(max_length=100)
    Maths=models.TextField(max_length=100)
    Gujarati=models.TextField(max_length=100)
    Computer=models.TextField(max_length=100)
    Sanskrit=models.TextField(max_length=100)
    Hindi=models.TextField(max_length=100)

class  AdminUserMaster(models.Model):
    Adm_Name = models.CharField(max_length=200)
    Adm_Email = models.EmailField()
    Adm_Contact = models.IntegerField()
    Adm_Password = models.TextField()
    Adm_Role = models.TextField()
    Adm_Status = models.BooleanField()