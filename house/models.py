from django.db import models

class Project(models.Model):
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    state = models.CharField(max_length=25)
    zip_code = models.PositiveIntegerField()
    bedroom = models.PositiveIntegerField()
    floor = models.PositiveIntegerField()
    image = models.ImageField(upload_to='templates/house/images')
    url = models.URLField(blank=True)