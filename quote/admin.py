from django.contrib import admin
from .models import marq


class MarqAdmin(admin.ModelAdmin):
    list_display = 'text',

admin.site.register(marq, MarqAdmin)
