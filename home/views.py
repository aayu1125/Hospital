from django.shortcuts import render, redirect
from .models import Department, Doctor
from .forms import DoctorCreationForm


def home(request):
    context = {
        'departments': Department.objects.all(),
        'doctors': Doctor.objects.select_related('department'),
    }
    return render(request, 'home.html', context)


def get_doctors_by_department(request):
    context = {
        'doctors': Doctor.objects.select_related('department'),
    }
    return render(request, 'doctors.html', context)

def create_doctor(request):
    form = DoctorCreationForm()
    if request.method == 'POST':
        form = DoctorCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_doctors_by_department')  #
    context = {
        'form': form
    }
    return render(request, 'create_doctor.html', context)