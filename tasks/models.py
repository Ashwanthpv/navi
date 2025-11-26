from django.db import models
from clients.models import Client

class Task(models.Model):
    PRIORITY = [('Low','Low'),('Medium','Medium'),('High','High')]

    title = models.CharField(max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
