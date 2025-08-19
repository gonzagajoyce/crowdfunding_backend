from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Additional fields can be added here if needed
    def __str__(self):
        return self.username
    


# Create your models here.
