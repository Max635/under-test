from django.apps import AppConfig


class LicenseEmailingApiConfig(AppConfig):
    name = 'license_emailing_api'

    def ready(self):
        from  license_emailing_api.emailManager import updater
        updater.start()
