from django.db import models
from django.contrib import admin
# Create your models here.

class Choice(models.Model):
    currency = models.CharField(max_length=3)
    #name = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.currency
    

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ["currency"]


