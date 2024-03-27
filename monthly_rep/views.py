from django.shortcuts import render, redirect
from .models import MonthlyReport
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

@login_required
def view_reports(request):
    reports = MonthlyReport.objects.filter(user=request.user)
    return render(request, 'reports.html', {'reports': reports})


@login_required
def submit_report(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        MonthlyReport.objects.create(user=request.user, content=content)
        return redirect('view_reports')
    return render(request, 'submit_report.html')


def home(request):
    return render(request, 'monthly_rep/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
