from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'highest_degree', 'wait_time', 'location', 'experience', 'fee', 'number_of_patients', 'satisfaction_level')
    list_filter = ('specialization', 'wait_time', 'location')
    search_fields = ['name', 'specialization', 'location']

admin.site.register(Doctor, DoctorAdmin)
