from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_max(value):
        '''Determines if value is entered is between 0 and 10'''
        if value < 0 or value > 10:
            raise ValidationError(
                _("%(value)s needs to be a value between 0 and 10, including 0 and 10, yada yada yada"),
                params = {"value": value},
            )

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name
    
class Attractions(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="attractions")
    name = models.CharField(max_length=100)
    outdoors = models.BooleanField()
    photo_url = models.TextField(default="no picture")

    def __str__(self):
        return self.name
    
class Reviews(models.Model):
    attraction = models.ForeignKey(Attractions, on_delete=models.CASCADE, related_name="reviews")
    reviewer = models.CharField(max_length=100, default = "not important")
    score = models.IntegerField(validators=[validate_max])
    review = models.TextField()
    reviews = models.CharField(default="This is for __str__ no inputs >:(")

    def __str__(self):
        return self.reviewer
    