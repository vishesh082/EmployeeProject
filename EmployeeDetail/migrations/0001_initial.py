# Generated by Django 2.1 on 2021-02-08 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.BigIntegerField()),
                ('person_type', models.CharField(max_length=10)),
                ('fname', models.CharField(max_length=50)),
                ('father', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('religion', models.CharField(max_length=10)),
                ('sex', models.CharField(max_length=1)),
                ('nation', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
