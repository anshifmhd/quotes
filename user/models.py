from django.db import models

# Create your models here.




class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.BigIntegerField()
    

class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Quotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quotes = models.CharField(max_length=1000)
    status = models.CharField(max_length=100, default="pending")

