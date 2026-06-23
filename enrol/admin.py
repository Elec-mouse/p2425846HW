from django.contrib import admin
from .models import Course, Grade

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','year','teacher')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student','course','grade')