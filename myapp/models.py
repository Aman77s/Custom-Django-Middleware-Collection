from django.db import models

# Create your models here.
class LoggingRecord(models.Model):
    ip = models.GenericIPAddressField()
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.ip} visited {self.path} at {self.timestamp}"
    