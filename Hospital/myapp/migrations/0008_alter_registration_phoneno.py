# Generated by Django 3.2.6 on 2021-08-10 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_registration_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='phoneno',
            field=models.CharField(max_length=12),
        ),
    ]
