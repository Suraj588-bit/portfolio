from django.db import models

# Create your models here.
class Job(models.Model):
    img = models.ImageField(upload_to='media/images/')
    summary = models.CharField(max_length=200)
    
    def __str__(self):
        return self.summary