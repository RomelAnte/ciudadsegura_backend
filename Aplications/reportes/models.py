from django.db import models

# Create your models here.
class Report(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    picture = models.ImageField(upload_to='report_pictures/', null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address
