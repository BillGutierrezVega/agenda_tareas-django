# Generated by Django 4.1.7 on 2023-11-20 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='public_fecha',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
