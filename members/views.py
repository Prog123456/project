from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import TimeIn, TimeOut, LunchIn, LunchOut

def index(request):
    return render(request, "index.html")


def time_in(request):
    if request.method == 'POST':
        TimeIn.objects.create()
        messages.success(request, 'Time in Registered', extra_tags='alert alert-success alert-dismissible show')
        return redirect('index')
    return render(request, "index.html")


def lunch_in(request):
    if request.method == 'POST':
        LunchIn.objects.create()
        messages.success(request, 'Lunch in Registered', extra_tags='alert alert-success alert-dismissible show')
        return redirect('index')
    return render(request, "index.html")


def lunch_out(request):
    if request.method == 'POST':
        LunchOut.objects.create()
        messages.success(request, 'Lunch out Registered', extra_tags='alert alert-success alert-dismissible show')
        return redirect('index')
    return render(request, "index.html")


def time_out(request):
    if request.method == 'POST':
        TimeOut.objects.create()
        messages.success(request, 'Time out Registered', extra_tags='alert alert-success alert-dismissible show')
        return redirect('index')
    return render(request, "index.html")


def attendance(request):
    if request.method == 'GET' and 'year' in request.GET and 'month' in request.GET:
        year = int(request.GET.get('year'))
        month = int(request.GET.get('month'))
        
        time_in_data = TimeIn.objects.filter(clicked_date__year=year, clicked_date__month=month)
        lunch_in_data = LunchIn.objects.filter(clicked_date__year=year, clicked_date__month=month)
        lunch_out_data = LunchOut.objects.filter(clicked_date__year=year, clicked_date__month=month)
        time_out_data = TimeOut.objects.filter(clicked_date__year=year, clicked_date__month=month)

        attendance_data = {}
        
        for entry in time_in_data:
            date_str = entry.clicked_date.strftime('%d-%m-%Y')
            attendance_data.setdefault(date_str, {})['timeIn'] = entry.clicked_time.strftime('%H:%M:%S')

        for entry in lunch_in_data:
            date_str = entry.clicked_date.strftime('%d-%m-%Y')
            attendance_data.setdefault(date_str, {})['lunchIn'] = entry.clicked_time.strftime('%H:%M:%S')

        for entry in lunch_out_data:
            date_str = entry.clicked_date.strftime('%d-%m-%Y')
            attendance_data.setdefault(date_str, {})['lunchOut'] = entry.clicked_time.strftime('%H:%M:%S')

        for entry in time_out_data:
            date_str = entry.clicked_date.strftime('%d-%m-%Y')
            attendance_data.setdefault(date_str, {})['timeOut'] = entry.clicked_time.strftime('%H:%M:%S')

        return JsonResponse(attendance_data)

    return render(request, 'attendance.html')