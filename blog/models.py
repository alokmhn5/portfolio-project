from django.db import models

# Create your models here.

class Blog(models.Model):
    topic = models.CharField(max_length = 255)
    created_on = models.DateTimeField()
    text = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.topic

    def summary(self):
        return self.text[:100]

    def created_on_pretty(self):
        return self.created_on.strftime('%b %e %Y')

#add  the blog app to settings
#Create a migration
#migrate
#register to admin
