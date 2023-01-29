# Generated by Django 4.1.5 on 2023-01-29 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensordata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('time', models.TimeField(auto_now_add=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensordata.sensor')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensordata.measure')),
            ],
        ),
    ]
