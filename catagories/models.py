from django.db import models

# Create your models here.
class catagories(models.Model):
    name=models.CharField(max_length=264)
    
    def __str__(self):
        return self.name