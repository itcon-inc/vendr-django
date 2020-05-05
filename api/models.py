from django.db import models

class City(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    rank = models.IntegerField()

    def __str__(self):
        return self.city
