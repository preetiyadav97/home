
from django.db import models

# Create your models here.
class Employee_detail(models.Model):
    name = models.CharField(max_length=30)
    department = models.CharField(max_length=20)
    email = models.EmailField()
    number=models.IntegerField(unique=True)
    # image=models.ImageField()
    
    def __str__(self):
        return self.name
    
    

