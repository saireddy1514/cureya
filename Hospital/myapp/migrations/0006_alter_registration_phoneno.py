# Generated by Django 3.2.6 on 2021-08-10 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210810_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='phoneno',
            field=models.CharField(max_length=100),
        ),
    ]