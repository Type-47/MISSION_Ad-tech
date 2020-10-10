from django.db import models

# Create your models here.
class User_Info(models.Model):
    userid = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    referrer = models.CharField(max_length=100)
    count = models.CharField(max_length=100)

    def __str__(self):
        return self.userid

