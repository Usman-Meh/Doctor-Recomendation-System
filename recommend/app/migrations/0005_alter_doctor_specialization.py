# Generated by Django 5.0.4 on 2024-04-28 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_doctor_specialization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(max_length=255),
        ),
    ]