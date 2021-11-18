# Generated by Django 3.2.8 on 2021-11-18 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0028_auto_20211118_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dhaxalayaal',
            name='Parcel',
        ),
        migrations.RemoveField(
            model_name='parcel',
            name='Purchaseinfo',
        ),
        migrations.RemoveField(
            model_name='purchaseinfo',
            name='Registrationid',
        ),
        migrations.RemoveField(
            model_name='purchaseinfo',
            name='identification',
        ),
        migrations.RemoveField(
            model_name='sellerinfo',
            name='parcel',
        ),
        migrations.RemoveField(
            model_name='supportingdoc',
            name='Parcel',
        ),
        migrations.AddField(
            model_name='purchaseinfo',
            name='RegistrationID',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='mainapp.parcel'),
        ),
        migrations.AlterField(
            model_name='dhaxalayaal',
            name='RegistrationNO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.parcel'),
        ),
        migrations.AlterField(
            model_name='identification',
            name='RegistrationNO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.parcel'),
        ),
        migrations.AlterField(
            model_name='sellerinfo',
            name='RegistrationNO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.parcel'),
        ),
        migrations.AlterField(
            model_name='supportingdoc',
            name='RegistrationNO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.parcel'),
        ),
    ]