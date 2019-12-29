from django.db import models
from django.utils import timezone

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    security_code = models.CharField(max_length=5)
    free_zone = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u"{0}:{1}... ".format(self.id, self.message[:10])
