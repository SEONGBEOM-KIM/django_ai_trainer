# Generated by Django 3.0.6 on 2020-06-10 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20200601_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='events',
            field=models.ManyToManyField(blank=True, to='events.MeasurementItem'),
        ),
    ]