from django.db import models
#from django.utils import timezone

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Netflix(models.Model):
    link = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    sub_genre = models.CharField(max_length=500)
    #date_created = models.DateTimeField(default=timezone.now)
