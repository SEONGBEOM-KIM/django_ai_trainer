# Generated by Django 3.1 on 2020-08-22 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20200822_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
    ]
