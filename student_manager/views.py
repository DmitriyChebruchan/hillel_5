from django.shortcuts import render
from faker import Faker
from django.http import HttpResponse


def index_page(request):
    return render(request, 'index.html')


def generate_student(request):
    return render(request, 'student_generator.html')


def generate_students(request):
    try:
        count = int(request.GET.get('count'))
        if 0 <= count <= 100:
            return HttpResponse('success')
        else:
            return HttpResponse('error')
    except ValueError:
        return HttpResponse('error')

