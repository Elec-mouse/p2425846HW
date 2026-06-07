from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Course(models.Model):
    year = models.IntegerField()
    name = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ("name", "year", )

    def __str__(self):
        return f"{self.name}({self.year})"

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return f"{self.student.username}-{self.course.name}:{self.grade}"
