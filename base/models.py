"""
Definition of models.
"""

from django.db import models

class item(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
