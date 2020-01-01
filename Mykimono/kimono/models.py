from django.db import models
from django.utils import timezone

GENDER_CHOICES = [
    ("0", "Not know"),
    ("1", "Male"),
    ("2", "FeMale"),
    ("9", "Not applicable"),
]

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    gender = models.CharField("gender", max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=50)
    mobile_number = models.IntegerField()
    hotel = models.CharField("Hotel", max_length=50)
    hotel_another = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    kimono_select = models.CharField("kimono", max_length=5)
    pay_type = models.CharField("Pay Type", max_length=10)
    card_number = models.IntegerField()
    expiry_date = models.CharField("Expiry Date", max_length=10)
    expiry_year = models.CharField("year", max_length=10)
    security_code = models.CharField(max_length=5)
    free_zone = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u"{0}:{1}... ".format(self.id, self.message[:10])
