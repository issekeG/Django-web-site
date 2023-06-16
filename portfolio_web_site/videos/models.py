from django.db import models


# Create your models here.


class Menu(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=150)
    descrition = models.TextField(max_length=1000)
    video_link = models.URLField(max_length=500)
    notebook = models.FileField(upload_to='static/notebooks/')
    date_creation = models.DateTimeField(auto_now_add=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    deployment = models.BooleanField(default=False)

    def __str__(self):
        return self.title
