# Generated by Django 3.2.8 on 2021-11-12 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_sellerinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SupportingDOC',
            fields=[
                ('RegistrationID', models.AutoField(primary_key=True, serialize=False)),
                ('IDcard', models.FileField(null=True, upload_to='IDCARD/')),
                ('GentalReciptVoucher', models.FileField(null=True, upload_to='GR/')),
                ('MasterPlan', models.FileField(null=True, upload_to='Masterplan/')),
                ('NotaryAuthorization', models.FileField(null=True, upload_to='NA/')),
                ('UploadCustomRegisForm', models.FileField(null=True, upload_to='UCR/')),
                ('Hibyan', models.FileField(null=True, upload_to='Hibyan/')),
                ('Dhaxal', models.FileField(null=True, upload_to='Dhaxal/')),
                ('FileScan', models.FileField(null=True, upload_to='Filescan/')),
                ('Parcel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.parcel')),
            ],
        ),
        migrations.CreateModel(
            name='DhaxalSubDoc',
            fields=[
                ('RegistrationID', models.AutoField(primary_key=True, serialize=False)),
                ('KalawarejinDOC1', models.FileField(null=True, upload_to='kalaDOC1/')),
                ('KalawarejinDOC2', models.FileField(null=True, upload_to='kalaDOC2/')),
                ('KalawarejinDOC3', models.FileField(null=True, upload_to='kalaDOC3/')),
                ('KalawarejinDOC4', models.FileField(null=True, upload_to='kalaDOC4/')),
                ('Parcel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.parcel')),
            ],
        ),
        migrations.CreateModel(
            name='Dhaxalayaal',
            fields=[
                ('Registrationid', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=500)),
                ('SecondName', models.CharField(max_length=500)),
                ('LastName', models.CharField(max_length=500)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=100)),
                ('Telephone', models.CharField(max_length=500)),
                ('Parcel', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainapp.parcel')),
            ],
        ),
    ]
