from django.db import models

class ServiceRequest(models.Model):
    TYPES_CHOICES = (
        ('Type1', 'Type 1'),
        ('Type2', 'Type 2'),
        ('Type3', 'Type 3'),
    )

    type = models.CharField(max_length=100, choices=TYPES_CHOICES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Service Request {self.pk}: {self.type}"
