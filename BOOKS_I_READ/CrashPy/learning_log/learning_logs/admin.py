from django.contrib import admin

# Register your models here.

from .models import Topic , Entry
#dot before tell django look file in same dir as admin.py

admin.site.register(Topic)
#tells django to manage model thru admin site

admin.site.register(Entry)
