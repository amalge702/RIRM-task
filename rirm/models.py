from django.db import models

# Create your models here.
class Register(models.Model):
    id = models.AutoField(auto_created = True,primary_key = True)
    Name = models.CharField(max_length=30)
    URL = models.URLField(max_length = 200)
    phone_number = models.CharField(max_length=12)


