# Generated by Django 4.1.3 on 2022-12-01 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('regular', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('dni', models.IntegerField()),
                ('direccion', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Menues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plato', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
