from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .models import Course, Grade
from django.contrib.auth import get_user_model

User = get_user_model()


def home(request):
    return render(request, 'enrol/home.html')


def course_list(request):
    all_course = Course.objects.all()
    return render(request, 'enrol/course_list.html', {'courses': all_course})


@login_required
def course_detail(request, pk):
    one_course = Course.objects.get(pk=pk)
    all_grade = Grade.objects.filter(course=one_course)
    return render(request, 'enrol/course_detail.html', {
        'course': one_course,
        'grades': all_grade
    })


@login_required
def student_list(request):
    if not request.user.is_staff:
        return HttpResponseForbidden(
            '<h1>403 Forbidden</h1><p>You do not have permission to access this page.</p>'
        )
    query = request.GET.get('q', '')
    if query:
        stu_list = User.objects.filter(
            username__startswith='p',
            username__icontains=query
        )
    else:
        stu_list = User.objects.filter(username__startswith='p')
    return render(request, 'enrol/student_list.html', {
        'students': stu_list,
        'query': query
    })


@login_required
def student_detail(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden(
            '<h1>403 Forbidden</h1><p>You do not have permission to access this page.</p>'
        )
    stu = User.objects.get(pk=pk)
    stu_grade = Grade.objects.filter(student=stu)
    return render(request, 'enrol/student_detail.html', {
        'student': stu,
        'grades': stu_grade
    })


def fail_student(request):
    fail_data = Grade.objects.filter(grade__lt=60)
    return render(request, 'enrol/fail.html', {'fail_list': fail_data})


@login_required
def my_grade(request):
    grades = Grade.objects.filter(student=request.user)
    return render(request, 'enrol/my_grade.html', {'grades': grades})


@login_required
def add_grade(request):
    if not request.user.is_staff:
        return HttpResponseForbidden(
            '<h1>403 Forbidden</h1><p>You do not have permission to access this page.</p>'
        )

    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        course_id = request.POST.get('course_id')
        grade_value = request.POST.get('grade')

        try:
            student = User.objects.get(pk=student_id)
            if student.username in ['p2499999', 's240002']:
                messages.error(request, 'Cannot modify data for this user.')
                return redirect('add_grade')
        except User.DoesNotExist:
            messages.error(request, 'Student not found.')
            return redirect('add_grade')

        course = Course.objects.get(pk=course_id)
        grade_obj, created = Grade.objects.update_or_create(
            student=student,
            course=course,
            defaults={'grade': grade_value}
        )
        msg = 'Grade added successfully.' if created else 'Grade updated successfully.'
        messages.success(request, msg)
        return redirect('add_grade')

    students = User.objects.filter(username__startswith='p')
    courses = Course.objects.all()
    return render(request, 'enrol/add_grade.html', {
        'students': students,
        'courses': courses
    })