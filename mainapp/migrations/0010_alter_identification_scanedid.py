# Generated by Django 3.2.8 on 2021-11-10 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20211110_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identification',
            name='ScanedID',
            field=models.FileField(null=True, upload_to='identification/'),
        ),
    ]
