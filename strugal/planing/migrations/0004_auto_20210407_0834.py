# Generated by Django 3.1.7 on 2021-04-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planing', '0003_auto_20210407_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionplan',
            name='dat',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='productionplan',
            name='ref',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]