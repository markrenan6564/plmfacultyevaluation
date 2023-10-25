from django.db import models

# Create your models here.
class Room(models.Model):
    USER_TYPES = (
        ('Applicant', 'Applicant'),
        ('Faculty', 'Faculty'),
        ('Admin', 'Admin'),
    )
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    facultyNum = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='Applicant')
