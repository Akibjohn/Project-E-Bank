# Generated by Django 3.2.8 on 2021-11-25 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='adharno',
            new_name='aadharno',
        ),
    ]