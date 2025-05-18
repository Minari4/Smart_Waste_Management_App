from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

class WasteBin(models.Model):
    BIN_TYPE_CHOICES = [
        ('recyclable', 'Recyclable'),
        ('organic', 'Organic'),
        ('general', 'General'),
    ]

    STATUS_CHOICES = [
        ('empty', 'Empty'),
        ('half', 'Half Full'),
        ('full', 'Full'),
    ]

    identifier = models.CharField(max_length=100, unique=True)
    bin_type = models.CharField(max_length=20, choices=BIN_TYPE_CHOICES)
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    current_status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    last_collected = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'bins_waste_bin'  # Use a unique table name for the WasteBin model

    def __str__(self):
        return self.identifier

    def get_absolute_url(self):
        return reverse('bin_detail', args=[str(self.id)])