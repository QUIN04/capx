import datetime

from django.db import models
from django.utils import timezone


class Bug(models.Model):
    description = models.CharField(max_length=300)
    bug_type = models.CharField(max_length=200)
    report_date = models.DateTimeField("date published")
    STATUS_CHOICES = [
     ('O', 'Open'),
     ('C', 'Closed'),
     ('IP', 'In Progress'),
     
     #Open - Indicates its a new a bug
     #In Progress - indicates the bug is under investigation and repair
     #Closed - Refers to a fixed in the system
     
    ]
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)

def __str__(self):
  return self.bug_text


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def __str__(self):
	    return self.bug_text
    