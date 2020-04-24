from django.db import models
from django.utils import timezone

# Create your models here.


class People(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    name = models.ForeignKey(
        People, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=200)
    create_data = models.DateTimeField(default=timezone.now)
    objects = models.Manager()

    def __str__(self):
        return str(self.title)
