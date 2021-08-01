from django.contrib import admin

from S5.models import Data
from django.contrib import admin

class datadisplay (admin.ModelAdmin):
    ListDisplay = ['Name', 'Age', 'Email', 'Adress']

admin.site.register(Data, datadisplay)