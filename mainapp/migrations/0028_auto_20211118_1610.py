# Generated by Django 3.2.8 on 2021-11-18 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0027_auto_20211118_1251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sellerinfo',
            old_name='Parcel',
            new_name='parcel',
        ),
        migrations.AlterField(
            model_name='identification',
            name='RegistrationNO',
            field=models.CharField(max_length=200),
        ),
    ]