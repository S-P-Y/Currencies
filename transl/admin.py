from django.contrib import admin
from transl.models import Choice, ChoiceAdmin




# Register your models here.
admin.site.register(Choice, ChoiceAdmin)
