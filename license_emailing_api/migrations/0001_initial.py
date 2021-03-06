# Generated by Django 3.1.6 on 2021-02-10 18:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerLicenseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='teste', max_length=50, verbose_name='Nome do cliente')),
                ('email', models.EmailField(max_length=50, verbose_name='E-mail')),
                ('license_code', models.CharField(editable=False, max_length=50, null=True)),
                ('license_init_date', models.DateField(default=datetime.date.today, editable=False)),
                ('package_name', models.CharField(choices=[('Professional', 'Professional'), ('Enterprise', 'Enterprise'), ('Community', 'Community')], max_length=12, verbose_name='Nome do Pacote')),
                ('license_type', models.CharField(choices=[('Quadrimensal', 'Quadrimensal'), ('Mensal', 'Mensal'), ('Semanal', 'Semanal')], max_length=12, verbose_name='Tempo de expiração da licença')),
                ('license_due_date', models.DateField(editable=False)),
            ],
            options={
                'db_table': 'customerlicense',
            },
        ),
    ]
