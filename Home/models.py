from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.email

class Registration(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
        
    