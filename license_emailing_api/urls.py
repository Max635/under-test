from django.urls import path, include
from . import views
from rest_framework import routers

from license_emailing_api.views import LicensesView, LicenseDueDateAPIView

router = routers.DefaultRouter()
router.register('licenses', views.LicensesView, basename='licenses_list')
router.register('due-date', views.LicenseDueDateAPIView, basename='duedate_list')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls
