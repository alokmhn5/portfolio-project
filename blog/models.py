from django.db import models

# Create your models here.

class Blog(models.Model):
    topic = models.CharField(max_length = 255)
    created_on = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

#add  the blog app to settings
#Create a migration
#migrate
#register to admin
