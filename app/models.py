from django.db import models

# Create your models here.
class Song(models.Model):
    image = models.ImageField(upload_to="media/image")
    song = models.FileField(upload_to="media/songs")


    def __str__(self):
        return self.song.__str__()
