from django.shortcuts import render
from django.http import HttpResponse
from faker import Faker
from student_manager.models import Student


def index_page(request):
    return render(request, "index.html")


def generate_student(request):
    
    fake = Faker()
    new_student = Student(name=fake.name(), address=fake.address())
    new_student.save()

    return render(request, "student_generator.html")


def generate_students(request):
    try:
        count = int(request.GET.get("count"))
        if 0 <= count <= 100:
            i=0
            while i < count:
                fake = Faker()
                new_student = Student(name=fake.name(), address=fake.address())
                new_student.save()
                i += 1
            return HttpResponse("success")
        else:
            return HttpResponse("error: Quantity of students is out of range: <br>0 - 100")
    except ValueError:
        return HttpResponse("error: Quantity of students to be countable")
