from django.db import models

# Create your models here.
class ReportType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Report(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey('ReportType', on_delete=models.CASCADE)
    description = models.TextField()
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    picture = models.ImageField(upload_to='report_pictures/', null=True, blank=True)
    status = models.CharField(max_length=50, default='Pendiente')
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address

