from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class Community(models.Model):
    title = models.TextField(max_length = 100)
    date = models.DateTimeField()
    content = TextField()
    image = models.ImageField(upload_to='images/', blank=True, null = True)
    
    def  __str__(self):
        return self.title