from django.shortcuts import render
from .models import Course, Grade
from django.contrib.auth import get_user_model
User = get_user_model()

def home(request):
    return render(request, 'enrol/home.html')

def course_list(request):
    all_course = Course.objects.all()
    return render(request, 'enrol/course_list.html', {'courses':all_course})

def course_detail(request,pk):
    one_course = Course.objects.get(pk=pk)
    all_grade = Grade.objects.filter(course=one_course)
    return render(request,'enrol/course_detail.html',{'course':one_course,'grades':all_grade})

def student_list(request):
    stu_list = User.objects.filter(username__startswith='p')
    return render(request,'enrol/student_list.html',{'students':stu_list})

def student_detail(request,pk):
    stu = User.objects.get(pk=pk)
    stu_grade = Grade.objects.filter(student=stu)
    return render(request,'enrol/student_detail.html',{'student':stu,'grades':stu_grade})
def fail_student(request):
    fail_data = Grade.objects.filter(grade__lt=60)
    return render(request,'enrol/fail.html',{'fail_list':fail_data})