from django.contrib import admin
from django.urls import path , include
from app import views 

from .views import load_data_from_csv, home , doctor_list
urlpatterns = [
    path('', home, name='home'),
    path('load-data-from-csv/', load_data_from_csv, name='load_data_from_csv'),
    path('doctor-list/', doctor_list, name='doctor_list'),
    

]

# urls.py
