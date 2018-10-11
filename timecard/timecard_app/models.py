from django.db import models


class TimeSheet(models.Model):
    name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    subject =models.CharField(max_length=200)
    hours = models.IntegerField()
    dateOfWork = models.DateTimeField()
    dateOfEntry = models.DateTimeField()

def __str__(self):
    return self.name