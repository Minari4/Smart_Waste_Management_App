from django.db import models
from django.contrib.auth.models import User
from bins.models import WasteBin  # Import WasteBin model

class Bin(models.Model):
    identifier = models.CharField(max_length=100)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'routes_bin_table'  # Use a unique table name for the Bin model

    def __str__(self):
        return self.identifier


class CollectionRoute(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    bins = models.ManyToManyField(
        WasteBin,
        through='RouteBin',
        related_name='collection_routes'
    )
    assigned_to = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='routes_assigned'  # Add a unique related_name
    )
    collection_day = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    
    point_a_latitude = models.FloatField(null=True, blank=True)
    point_a_longitude = models.FloatField(null=True, blank=True)
    point_b_latitude = models.FloatField(null=True, blank=True)
    point_b_longitude = models.FloatField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='', blank=True, null=True)

    def __str__(self):
        return self.name


class RouteBin(models.Model):
    route = models.ForeignKey(
        'CollectionRoute', 
        on_delete=models.CASCADE, 
        related_name='route_bins'
    )
    bin = models.ForeignKey(
        WasteBin,
        on_delete=models.CASCADE, 
        related_name='route_bin_links'
    )
    collection_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['collection_order']
        unique_together = ('route', 'bin')
        db_table = 'routes_route_bin'  # Use a unique table name for the RouteBin model

    def __str__(self):
        return f"{self.route.name} - {self.bin.identifier} (Order: {self.collection_order})"