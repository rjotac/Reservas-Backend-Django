# Generated by Django 2.1.5 on 2019-08-11 05:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservas',
            name='precio',
            field=models.CharField(default=django.utils.timezone.now, max_length=4),
            preserve_default=False,
        ),
    ]
