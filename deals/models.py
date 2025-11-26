from django.db import models

class Deal(models.Model):
    DEAL_STATUS = (
        ('open', 'Open'),
        ('won', 'Won'),
        ('lost', 'Lost'),
    )

    name = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.CharField(max_length=200)
    stage = models.CharField(max_length=50, choices=DEAL_STATUS, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
 