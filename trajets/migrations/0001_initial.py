# Generated by Django 5.1.1 on 2024-09-20 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Itineraire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('start_lat', models.FloatField()),
                ('start_lng', models.FloatField()),
                ('end_lat', models.FloatField()),
                ('end_lng', models.FloatField()),
            ],
        ),
    ]
