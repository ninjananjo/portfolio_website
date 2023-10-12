from django.db import models
import datetime
from PIL import Image


class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    project_name = models.CharField(default='my project', max_length=100)
    summary = models.TextField()
    date_completed = models.DateField(default=datetime.date.today)
    link = models.URLField(default='https://github.com/ninjananjo/', blank=True)

    def __str__(self):
        return self.project_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.name)
        if img.height > 450 or img.width > 800:
            output_size = (450, 800)
            img.thumbnail(output_size)
            img.save(self.image.name)


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=1000)
    datetime_sent = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
