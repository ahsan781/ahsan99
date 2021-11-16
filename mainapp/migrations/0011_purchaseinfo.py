# Generated by Django 3.2.8 on 2021-11-11 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_identification_scanedid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchaseinfo',
            fields=[
                ('RegistrationNO', models.AutoField(primary_key=True, serialize=False)),
                ('OwnerFirstName', models.CharField(max_length=500)),
                ('OwnerSecondName', models.CharField(max_length=500)),
                ('OwnerLastName', models.CharField(max_length=500)),
                ('OwnerSurName', models.CharField(max_length=500)),
                ('Mobile', models.CharField(max_length=500)),
                ('Email', models.CharField(max_length=500)),
                ('OtherProperty', models.CharField(max_length=500)),
                ('District', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.district')),
                ('Neighbor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.neighbor')),
                ('PlotNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.plotno')),
                ('SubDistrict', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.subdistrict')),
                ('identification', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.identification')),
            ],
        ),
    ]