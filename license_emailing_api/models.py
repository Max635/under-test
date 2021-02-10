from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from django.db import models


class CustomerLicenseModel(models.Model):
    class Meta:
        db_table = 'customerlicense'

    PACKAGE_CHOICES = (
        ('Professional', 'Professional'),
        ('Enterprise', 'Enterprise'),
        ('Community', 'Community')
    )
    TYPE_CHOICES = (
        ('Quadrimensal', 'Quadrimensal'),
        ('Mensal', 'Mensal'),
        ('Semanal', 'Semanal')
    )

    name = models.CharField('Nome do cliente', default='teste', max_length=50)
    email = models.EmailField('E-mail', max_length=50)
    license_code = models.CharField(max_length=50, null=True, editable=False)
    license_init_date = models.DateField(default=date.today, editable=False)
    package_name = models.CharField('Nome do Pacote', max_length=12, choices=PACKAGE_CHOICES, blank=False, null=False)
    license_type = models.CharField('Tempo de expiração da licença', max_length=12, choices=TYPE_CHOICES, blank=False, null=False)
    license_due_date = models.DateField(editable=False)

    def save(self, *args, **kwargs):
        self.license_code = datetime.timestamp(datetime.now())
        if self.license_type == 'Quadrimensal':
            self.license_due_date = self.license_init_date + relativedelta(months=+4)
        elif self.license_type == 'Mensal':
            self.license_due_date = self.license_init_date + relativedelta(months=+1)
        else:
            self.license_due_date = self.license_init_date + relativedelta(weeks=1)
        super(CustomerLicenseModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
