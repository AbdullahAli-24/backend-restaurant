from django.db import models

# Create your models here.
role_choices = [
    ('customer', 'Customer'),   
    ('admin', 'Admin'),
]

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True )
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=role_choices, default='customer' )

    def __str__(self):
        return self.username