# Generated by Django 4.1.3 on 2022-12-30 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('devicemodel', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('devicemanufacturer', models.CharField(max_length=100)),
                ('devicetype', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'device',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empname', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('empage', models.IntegerField()),
                ('empdesignation', models.CharField(max_length=100)),
                ('empgender', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emptemperature', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('devicemodel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee_api.device')),
                ('empname', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee_api.employee')),
            ],
            options={
                'db_table': 'temperature',
            },
        ),
    ]
