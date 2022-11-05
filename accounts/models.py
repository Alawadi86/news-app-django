from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class CustomUser(AbstractUser):
    birthday = models.DateField(max_length=8)
    age = models.IntegerField()
    def __str__(self):
        today = date.today()

        age = today.year - dob.year
        if today.month < dob.month or today.month == dob.month and today.day < dob.day:
            age -= 1
        return self.age 



 





    


