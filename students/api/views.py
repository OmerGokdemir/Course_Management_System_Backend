from rest_framework import generics
from students.models import Teacher, Course, Student
from students.api.serializers import TeacherSerializer, CourseSerializer, StudentSerializer

class TeacherListCreateAPIView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all().order_by("id")
    serializer_class = TeacherSerializer
    
class TeacherDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all().order_by("id")
    serializer_class = TeacherSerializer
    
    
class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all().order_by("id")
    serializer_class = CourseSerializer
    
class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all().order_by("id")
    serializer_class = CourseSerializer
    
    
class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all().order_by("id")
    serializer_class = StudentSerializer
    
class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all().order_by("id")
    serializer_class = StudentSerializer
    
    
