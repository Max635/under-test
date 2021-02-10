from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import CustomerLicenseModel


class LicenseForm(forms.ModelForm):
    class Meta:
        model = CustomerLicenseModel
        fields = ['name', 'email', 'package_name', 'license_type']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar Licença'))
