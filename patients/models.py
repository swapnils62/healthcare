from django.db import models
from django.contrib.auth.models import User
from doctors.models import Doctor
# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='patients')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
