from audioop import reverse
from django.db import models

# Create your models here.
class Post(models.Model): #inheritance
    title = models.CharField(max_length=256) #composition
    subtitle = models.CharField(max_length=256)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail",args=[self.id])