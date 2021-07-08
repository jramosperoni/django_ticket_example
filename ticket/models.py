from django.db import models


class Priority(models.IntegerChoices):
    LOW = 0
    MEDIUM = 1
    HIGH = 2


class Ticket(models.Model):
    subject = models.CharField(max_length=50)
    description = models.TextField()
    priority = models.IntegerField(choices=Priority.choices, default=Priority.LOW)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']


class Message(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
