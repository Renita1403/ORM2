from django.db import models
from django.contrib import admin
class car(models.Model):
    car_name= models.CharField()
    car_model = models.CharField()
    release_date = models.DateField()

class carAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'car_model', 'release_date')
# Create your models here.
