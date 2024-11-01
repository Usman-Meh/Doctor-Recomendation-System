# Generated by Django 5.0.4 on 2024-04-27 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(choices=[('Dermatologist', 'Dermatologist'), ('Gynecologist', 'Gynecologist'), ('Urologist', 'Urologist'), ('Gastroenterologist', 'Gastroenterologist'), ('Neurologist', 'Neurologist'), ('ENT Specialist', 'ENT Specialist'), ('Psychiatrist', 'Psychiatrist'), ('Pediatrician', 'Pediatrician'), ('Dentist', 'Dentist'), ('Sexologist', 'Sexologist')], max_length=255),
        ),
    ]
