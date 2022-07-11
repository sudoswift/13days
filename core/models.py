from operator import truediv
from django.db import models

class TimeStampedModels(models.Model):
    """Time Stamped Model"""
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        abstract = True