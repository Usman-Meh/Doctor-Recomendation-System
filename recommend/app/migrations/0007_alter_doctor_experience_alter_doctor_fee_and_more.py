# Generated by Django 5.0.4 on 2024-05-02 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20240502_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='experience',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='fee',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='number_of_patients',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='wait_time',
            field=models.CharField(max_length=255),
        ),
    ]
