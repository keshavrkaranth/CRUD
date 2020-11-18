from django.db import models

# Create your models here.

class Student(models.Model):
    Name = models.CharField(max_length=30)
    Course = models.CharField(max_length=30)
    Phone_no = models.PositiveIntegerField()
    FatherName = models.CharField(max_length=30)

    def __str__(self):
        return self.Name
