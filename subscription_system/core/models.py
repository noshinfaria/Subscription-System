from django.db import models
from django.contrib.auth.models import User

class Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Subscription(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('cancelled', 'Cancelled'),
        ('expired', 'Expired'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.plan.name}"

class ExchangeRateLog(models.Model):
    base_currency = models.CharField(max_length=10)
    target_currency = models.CharField(max_length=10)
    rate = models.FloatField()
    fetched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.base_currency} to {self.target_currency} at {self.fetched_at}"

