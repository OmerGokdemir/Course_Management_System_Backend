from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.user.get_full_name()}"
    
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=True, null=True)
    schedule = models.TextField(blank=True, null=True)
    
    
    def __str__(self):
        return f"{self.name}"
    

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birth_date = models.DateField()
    registration_date = models.DateTimeField(auto_now_add=True)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    enrolled_course = models.ManyToManyField(Course, related_name="student")
    note = models.FloatField(
        validators=[MinValueValidator(1.00), MaxValueValidator(5,00)],
        blank=True, null=True
    )
    
    def __str__(self):
        return f"{self.user.get_full_name()}"
