from django.db import models


class Question(models.Model):
    ask = models.CharField(max_length=50)
    prompt1 = models.CharField(max_length=50, blank=True)
    prompt2 = models.CharField(max_length=50, blank=True)
    prompt3 = models.CharField(max_length=50, blank=True)
    prompt4 = models.CharField(max_length=50, blank=True)
    create_time = models.TimeField()
