# Generated by Django 3.2.6 on 2021-08-17 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20210817_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorregistration',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='registration',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]