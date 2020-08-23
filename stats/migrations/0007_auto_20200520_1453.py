# Generated by Django 3.0.6 on 2020-05-20 05:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stats', '0006_auto_20200518_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stat',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to=settings.AUTH_USER_MODEL),
        ),
    ]