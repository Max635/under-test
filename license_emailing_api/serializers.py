from rest_framework import serializers
from .models import CustomerLicenseModel


class LicensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerLicenseModel
        fields = ['id', 'name', 'email', 'license_code', 'package_name', 'license_type', 'license_due_date']
