from django.db import models
from django.utils import timezone

class info(models.Model):
    
    edcation_type =[
        ('CS','Computer Science'),
        ('AI','Artificial Intelligence')
        ('ML','Machine Learning')
    ]
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='image/')
    date = models.DateField(default=timezone.now)
    education = models.CharField(max_length=2, choices=edcation_type)