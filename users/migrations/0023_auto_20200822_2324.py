# Generated by Django 3.1 on 2020-08-22 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20200822_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bendFoward',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=4, null=True),
        ),
    ]