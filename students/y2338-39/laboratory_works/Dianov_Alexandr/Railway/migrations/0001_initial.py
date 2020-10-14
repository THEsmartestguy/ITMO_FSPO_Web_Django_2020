# Generated by Django 3.1.2 on 2020-10-09 11:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('RideId', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('DepartureTime', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('ArrivalTime', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('StartAt', models.CharField(db_index=True, max_length=150)),
                ('FinishAt', models.CharField(db_index=True, max_length=150)),
            ],
        ),
    ]