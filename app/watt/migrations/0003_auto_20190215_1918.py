# Generated by Django 2.1.7 on 2019-02-15 18:18

import app.watt.models
from django.db import migrations
import django_enumfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('watt', '0002_auto_20190215_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='energy_type',
            field=django_enumfield.db.fields.EnumField(default=0, enum=app.watt.models.EnergyType),
        ),
    ]
