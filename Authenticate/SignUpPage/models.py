from django.db import models

class Index(models.Model):
    username=models.CharField(max_length=120)
    fname=models.CharField(max_length=120)
    lname=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    password1=models.CharField(max_length=120)
    password2=models.CharField(max_length=120)
    def __str__(self):
        return self.name
