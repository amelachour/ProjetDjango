from django.db import models
<<<<<<< HEAD
from django.utils import timezone

class Cours(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='courses/')
    date_posted = models.DateTimeField(default=timezone.now)  
=======

class Cours(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='cours/')
    date_posted = models.DateTimeField(auto_now_add=True)
>>>>>>> c4f4019b0ff2ad6983f6bd24f6b5f3e4a8431bde

    def __str__(self):
        return self.title
