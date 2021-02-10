from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from license_emailing_api.views import LicensesView, LicenseDueDateAPIView


schema_view = get_swagger_view(title='API Documentation License Emailing')

router = routers.DefaultRouter()
router.register('licenses', views.LicensesView, basename='licenses_list')
router.register('due-date', views.LicenseDueDateAPIView, basename='duedate_list')

urlpatterns = [
    path('', include(router.urls)),
    path('api-docs/', schema_view),
]

urlpatterns += router.urls
