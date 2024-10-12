from django.db import models

class Cours(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    file = models.FileField(upload_to='cours/')
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
