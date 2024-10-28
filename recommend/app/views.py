# app/views.py
import os
import joblib
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from .models import Doctor, SPECIALIZATIONS
from sklearn.compose import make_column_transformer
import sklearn.preprocessing as pre_process
ordinal_encoding =pre_process.OrdinalEncoder()
standard_scaling  =pre_process.StandardScaler()

def home(request):
    if request.method == 'POST':
        min_fee = request.POST.get('min_fee')
        max_fee = request.POST.get('max_fee')
        experience = request.POST.get('experience')
        wait_time = request.POST.get('wait_time')
        location = request.POST.get('location')
        specializations = request.POST.getlist('specialization')
        # Filter doctors based on the provided input
        doctors = Doctor.objects.filter(
            fee__gte=min_fee,
            fee__lte=max_fee,
            experience__gte=experience,
            wait_time=wait_time,
            location__icontains=location,
            specialization__in=specializations
        ).order_by('experience', 'fee')

        return render(request, 'doctor_list.html', {'doctors': doctors})

    return render(request, 'home.html', {'SPECIALIZATIONS': SPECIALIZATIONS})

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})


def load_data_from_csv(request):
    # Load the machine learning model
    model = load_ml_model()
    file_path = 'app/Models/oladoc_file.csv'
    df = pd.read_csv(file_path)
    
    for index, row in df.iterrows():
        # Preprocess the data
        processed_data = preprocess_data(row)

       # Make predictions
        prediction = model.predict(processed_data.reshape(1, -1))

        # Check if the doctor is recommended
        if prediction == 1:
            Doctor.objects.create(
                name=row['Name: '],
                specialization=row['Specialization'],
                highest_degree=row['Highest degree: '],
                experience=row['Experience'],
                fee=row['Fee'],
                wait_time=row['Wait_time'],
                number_of_patients=row['NOP'],
                satisfaction_level=row['Satisfection_level'],
                location=row['Location']
            )
    return HttpResponse("Data Loaded Successfully!")

# Load the machine learning model
def load_ml_model():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(BASE_DIR, 'app\Models\ML_model.pkl')
    loaded_model = joblib.load(filename)
    return loaded_model


def preprocess_data(data):
    # Convert the data to a DataFrame
    df = pd.DataFrame([data])  # Convert Series to DataFrame

    # Remove colon from column names
    df.columns = df.columns.str.rstrip(':')

    # Drop 'Name' column if it exists
    if 'Name:' in df.columns:
        df.drop(['Name:'], inplace=True, axis=1)

    X = df  # Use DataFrame directly
    # Make column transformer
    transform_x = make_column_transformer(
        (ordinal_encoding,  ['Specialization', 'Highest degree: ', 'Wait_time','Location'])
           ,(standard_scaling,['Experience','Fee', 'Satisfection_level', 'NOP'])
    )

    # Apply transformations
    processed_x = transform_x.fit_transform(X)

    # Return the preprocessed data as a numpy array
    return processed_x




from .models import Doctor

def delete_all_doctors(request):
    # Delete all data from the Doctor model
    Doctor.objects.all().delete()
    
    # Return a response to indicate that data has been deleted
    return HttpResponse("All data from the Doctor model has been deleted.")
