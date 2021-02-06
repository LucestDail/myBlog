from django.db import models

# Create your models here.


class Post(models.Model):
    writer = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    mainphoto = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title
