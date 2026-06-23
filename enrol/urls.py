from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course/', views.course_list, name='course_list'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('student/', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('fail/', views.fail_student, name='fail'),
    path('myGrade/', views.my_grade, name='my_grade'),
    path('add_grade/', views.add_grade, name='add_grade'),
]
