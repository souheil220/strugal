# Generated by Django 3.2 on 2021-05-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rapport', '0002_auto_20210528_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapportjournaliera',
            name='n_of',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='rapportjournaliere',
            name='n_of',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='rapportjournalierlb',
            name='n_of',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='rapportjournalierlc',
            name='n_of',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='rapportjournalierrpt',
            name='n_of',
            field=models.CharField(max_length=255),
        ),
    ]
