# Generated by Django 3.2.3 on 2021-08-04 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapport', '0004_alter_rapportjournalieralr_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapportjournalieralr',
            name='date_created',
            field=models.CharField(default='2021-08-04', max_length=255),
        ),
        migrations.AlterField(
            model_name='rapportjournaliere',
            name='date_created',
            field=models.CharField(default='2021-08-04', max_length=255),
        ),
    ]
