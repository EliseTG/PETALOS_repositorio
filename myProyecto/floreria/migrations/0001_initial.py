# Generated by Django 2.2.6 on 2019-10-28 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nombre', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('contrasena', models.TextField()),
                ('correo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Floreria',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('valor', models.IntegerField()),
                ('estado', models.TextField()),
                ('stock', models.IntegerField()),
                ('foto', models.ImageField(null=True, upload_to='flores')),
            ],
        ),
    ]
