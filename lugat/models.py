from django.db import models

class Lugat(models.Model):
    english = models.CharField(max_length=128)
    uzbek = models.CharField(max_length=128)