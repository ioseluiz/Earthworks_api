# Generated by Django 5.1.1 on 2024-09-17 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Truck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('model', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('capacity', models.FloatField()),
            ],
        ),
    ]
