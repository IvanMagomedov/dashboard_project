from django.db import models

class SalesRecord(models.Model):
    date = models.DateField()
    product = models.CharField(max_length=100)
    amount = models.FloatField()

    def __str__(self):
        return f"{self.product} - {self.date} - {self.amount}"