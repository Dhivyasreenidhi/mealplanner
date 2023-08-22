from django.db import models
class contact(models.Model):
    Name = models.CharField(max_length = 250)
    PhoneNumber = models.IntegerField(max_length = 10)
    EmailId = models.CharField(max_length = 255)
    Message = models.CharField(max_length = 500)
class UserProfile(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=100)

