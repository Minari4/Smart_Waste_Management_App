from django.db import models
from django.contrib.auth import get_user_model
from bins.models import WasteBin

User = get_user_model()

class IllegalDumpingReport(models.Model):
    STATUS_CHOICES = (
        ('reported', 'Reported'),
        ('investigating', 'Investigating'),
        ('resolved', 'Resolved'),
    )
    
    reporter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    description = models.TextField()
    photo = models.ImageField(upload_to='%Y/%m/%d/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='reported')
    reported_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField(blank=True)
    
    def __str__(self):
        return f"Dumping at {self.location} - {self.get_status_display()}"
    
    class Meta:
        ordering = ['-reported_at']