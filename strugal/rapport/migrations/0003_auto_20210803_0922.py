# Generated by Django 3.2.3 on 2021-08-03 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapport', '0002_auto_20210802_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapportjournalieralr',
            name='date_created',
            field=models.CharField(default='2021-08-03', max_length=255),
        ),
        migrations.AlterField(
            model_name='rapportjournaliere',
            name='date_created',
            field=models.CharField(default='2021-08-03', max_length=255),
        ),
    ]
