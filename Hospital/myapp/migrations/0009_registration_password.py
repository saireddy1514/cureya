# Generated by Django 3.2.6 on 2021-08-10 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_registration_phoneno'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='password',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
