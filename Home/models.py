from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.email

class Register(models.Model):
        first_name = models.CharField(max_length=100)
        last_name = models.CharFeild(max_length=100)
        email = models.CharFeild(max_length=100)
        date = models.DateField()
        
        def __str__(self):
        return self.email
        
    