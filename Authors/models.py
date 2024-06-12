from django.db import models

# Create your models here.
class Authors(models.Model):
    name=models.CharField(max_length=264)
    bio = models.TextField(max_length=100)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name