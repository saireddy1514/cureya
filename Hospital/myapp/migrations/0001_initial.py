# Generated by Django 3.2.6 on 2021-08-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phoneno', models.IntegerField(max_length=10)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]