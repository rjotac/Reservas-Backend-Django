# Generated by Django 2.1.5 on 2019-03-01 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCategoria', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=200)),
                ('tipoCategoria', models.CharField(max_length=10)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('estado', models.IntegerField(max_length=1)),
            ],
        ),
    ]
