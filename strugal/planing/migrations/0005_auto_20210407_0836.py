# Generated by Django 3.1.7 on 2021-04-07 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planing', '0004_auto_20210407_0834'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productionplan',
            old_name='dat',
            new_name='date_created',
        ),
    ]
