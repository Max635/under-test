from django.shortcuts import render

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response

from .models import CustomerLicenseModel
from .serializers import LicensesSerializer
from .forms import LicenseForm


class LicensesView(viewsets.ModelViewSet):
    queryset = CustomerLicenseModel.objects.all()
    serializer_class = LicensesSerializer

class LicenseDueDateAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = CustomerLicenseModel.objects.all()
    serializer_class = LicensesSerializer
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ['license_due_date',]

class LicenseListView(ListView):
    model = CustomerLicenseModel
    context_object_name = 'license'

class LicenseCreateView(CreateView):
    model = CustomerLicenseModel
    fields = ['name', 'email', 'package_name', 'license_type']
    success_url = reverse_lazy('license_list')
