# Generated by Django 3.2.3 on 2021-07-29 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapport', '0006_auto_20210729_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapportjournalieralr',
            name='ref',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
