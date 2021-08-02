# Generated by Django 3.2.3 on 2021-08-01 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductionPlan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ref', models.CharField(blank=True, max_length=255)),
                ('qte', models.FloatField()),
                ('typeP', models.CharField(max_length=255)),
                ('date_created', models.CharField(blank=True, max_length=255)),
                ('planned', models.BooleanField()),
            ],
        ),
    ]
