# Generated by Django 3.2.8 on 2021-11-10 15:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_identification_iddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identification',
            name='ScanedID',
            field=models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'ppt', 'xlsx'])]),
        ),
    ]
