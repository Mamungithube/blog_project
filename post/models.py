from django.db import models
from catagories.models import catagories
from Authors.models import Authors
# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=64)
    content = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    category =models.ManyToManyField(catagories)
    Authors = models.ForeignKey(Authors,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.Authors.name}"