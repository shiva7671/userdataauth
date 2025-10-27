from django.db import models

# Create your models here.
class UserLoginModel(models.Model):
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=18)

    class Meta:
        abstract=True


class UserSignupModel(UserLoginModel):
    mail=models.EmailField(unique=True)
    mobile_number=models.IntegerField(unique=True)


class UserDetails(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    role=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
