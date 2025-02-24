from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PatientForm
from .models import Patient

# Add Patient
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('list_pat')
    
    else:
        form = PatientForm()

    return render(request, 'add_patient.html', {'form':form})

# List Patient
def list_patient(request):
    patient = Patient.objects.all()
    return render(request, 'list_patient.html', {'patients':patient})

# Update Patient Details
def update_patient(request, pk):
    patient = Patient.objects.get(patID=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)

        if form.is_valid():
            form.save()
            return redirect('list_pat')
        
    else:
        form = PatientForm(instance=patient)
    return render(request, 'update_patient.html', {'form':form})

# Delete Patient
def delete_patient(request, pk):
    patient = Patient.objects.get(patID=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('list_pat')