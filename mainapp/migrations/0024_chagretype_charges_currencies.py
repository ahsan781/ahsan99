# Generated by Django 3.2.8 on 2021-11-13 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_rename_bussinessrevenu_bussinessrevenu_bussinessreg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currencies',
            fields=[
                ('CurrCode', models.AutoField(primary_key=True, serialize=False)),
                ('CurrName', models.CharField(max_length=500)),
                ('ExcRate', models.CharField(max_length=500)),
                ('BussinessRevenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.bussinessrevenu')),
            ],
        ),
        migrations.CreateModel(
            name='Charges',
            fields=[
                ('ChargeCode', models.AutoField(primary_key=True, serialize=False)),
                ('ChargeName', models.CharField(max_length=500)),
                ('Glnaccount', models.CharField(max_length=500)),
                ('Chargestatus', models.CharField(max_length=500)),
                ('BussinessRevenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.bussinessrevenu')),
            ],
        ),
        migrations.CreateModel(
            name='ChagreType',
            fields=[
                ('ChagreType', models.AutoField(primary_key=True, serialize=False)),
                ('BussinessReg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.bussinessregistration')),
            ],
        ),
    ]
