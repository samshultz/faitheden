from django.contrib import admin
from .models import AboutUs


class AboutUsAdmin(admin.ModelAdmin):
    list_display = 'title', 'created', 'updated'

admin.site.register(AboutUs, AboutUs)