from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = 'title', 'created', 'updated'

admin.site.register(Payment, PaymentAdmin)