from django.db import models
from django.utils import timezone

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    create_data = models.DateTimeField(default=timezone.now)
    body = models.TextField(default='NOT_PROVIDED')

    def __str__(self):
        return str(self.name)

    def summary(self):
        return self.body[:100]
