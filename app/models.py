from django.db import models


# Create your models here.
class UserData(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
