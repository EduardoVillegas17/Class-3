from django.db import models

# Create your models here.
class Post(models.Model): #inheritance
    title = models.CharField(max_length=256) #composition
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)