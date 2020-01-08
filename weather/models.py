from django.db import models
from django.utils import timezone
# Create your models here.

class WH(models.Model):
    added_date = models.DateTimeField(default=timezone.now)
    text = models.CharField(max_length=50)
    temperature = models.CharField(max_length=10)
    descrip = models.CharField(max_length=10)
    icon = models.CharField(max_length=10)
