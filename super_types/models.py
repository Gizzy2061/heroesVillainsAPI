from django.db import models

# Create your models here

class Super_type(models.model):
    type = models.CharField(max_length=255)
    