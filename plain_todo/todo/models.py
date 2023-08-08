from django.db import models

# Create your models here.
class Task(models.Model):
    text = models.CharField(max_length=255)
    # category = models.CharField(macdefault=None)
    # date_modified = 
    date_created = models.DateTimeField(auto_now_add=True)
    isCompleted = models.BooleanField(default=False)
