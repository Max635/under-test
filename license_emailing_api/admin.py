from django.contrib import admin
from .models import CustomerLicenseModel


class CustomerAdmin(admin.ModelAdmin):
    fields = '__all__'

admin.site.register(CustomerLicenseModel)
