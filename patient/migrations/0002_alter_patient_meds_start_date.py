# Generated by Django 3.2.6 on 2021-08-06 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='meds_start_date',
            field=models.DateField(),
        ),
    ]
