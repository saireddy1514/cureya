# Generated by Django 3.2.6 on 2021-08-19 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_registration_patid'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorregistration',
            name='docid',
            field=models.CharField(default='', max_length=100),
        ),
    ]
