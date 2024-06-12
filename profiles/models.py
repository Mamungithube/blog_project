from django.db import models
from Authors.models import Authors
# Create your models here.
class profile(models.Model):
    name= models.CharField(max_length=255)
    about = models.TextField()
    Authors = models.OneToOneField(Authors,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.name