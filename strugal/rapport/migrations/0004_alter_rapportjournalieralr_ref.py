# Generated by Django 3.2.3 on 2021-08-03 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planing', '0003_auto_20210801_0844'),
        ('rapport', '0003_auto_20210803_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rapportjournalieralr',
            name='ref',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planing.productionplan'),
        ),
    ]
