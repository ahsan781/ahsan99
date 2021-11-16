# Generated by Django 3.2.8 on 2021-11-16 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_chagretype_charges_currencies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plotmap',
            name='RegistrationID',
        ),
        migrations.RemoveField(
            model_name='plotno',
            name='Propertymap',
        ),
        migrations.RemoveField(
            model_name='plotno',
            name='identification',
        ),
        migrations.RemoveField(
            model_name='propertymap',
            name='RegistrationID',
        ),
        migrations.AddField(
            model_name='plotmap',
            name='purchaseinfo',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='mainapp.purchaseinfo'),
        ),
        migrations.AddField(
            model_name='propertymap',
            name='Purchaseinfo',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='mainapp.purchaseinfo'),
        ),
    ]