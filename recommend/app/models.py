from django.db import models

# Create your models here.
# models.py

# models.py
SPECIALIZATIONS =[
    ('Dermatologist', 'Dermatologist'),
    ('Gynecologist', 'Gynecologist'),
    ('Urologist', 'Urologist'),
    ('Gastroenterologist', 'Gastroenterologist'),
    ('Neurologist', 'Neurologist'),
    ('ENT Specialist', 'ENT Specialist'),
    ('Psychiatrist', 'Psychiatrist'),
    ('Pediatrician', 'Pediatrician'),
    ('Dentist', 'Dentist'),
    ('Sexologist', 'Sexologist'),
]

   
class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    highest_degree = models.CharField(max_length=255) 
    experience = models.FloatField()
    fee = models.FloatField()
    wait_time = models.CharField(max_length=255)
    number_of_patients = models.FloatField()
    satisfaction_level = models.IntegerField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name
