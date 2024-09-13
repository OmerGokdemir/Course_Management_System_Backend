from django.test import TestCase
from django.contrib.auth import get_user_model
from students.models import Teacher, Course, Student
from datetime import date


User = get_user_model()


# Model Tests


class TeacherModelTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            email="teacheruser@email.com",
            password="Teacherpass123",
            first_name="Teacher",
            last_name="User"
        )
        
        
        
    def test_create_teacher(self):
        teacher = Teacher.objects.create(
            user=self.user,
            specialization="Mathematics"
        )
        
        self.assertEqual(teacher.user.email, "teacheruser@email.com")
        self.assertEqual(str(teacher), "Teacher User")
        self.assertEqual(teacher.specialization, "Mathematics")
        
        
class CourseModelTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            email="teacheruser@email.com",
            password="Teacherpass123",
            first_name="Teacher",
            last_name="User"
        )
        self.teacher = Teacher.objects.create(
            user=self.user,
            specialization="Mathematics"
        )
        
        
    def test_create_course(self):
        course = Course.objects.create(
            name="Calculus",
            code="MATH101",
            teacher=self.teacher,
            schedule="Mon-Wed-Fri 09:00-10:30"
        )
        
        self.assertEqual(course.name, "Calculus")
        self.assertEqual(course.code, "MATH101")
        self.assertEqual(course.teacher, self.teacher)
        self.assertEqual(str(course), "Calculus")
        
        
class StudentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="teacheruser@email.com",
            password="Teacherpass123",
            first_name="Teacher",
            last_name="User"
        )
        self.teacher = Teacher.objects.create(
            user=self.user,
            specialization="Mathematics"
        )
        self.student_user = User.objects.create_user(
            email="studentuser@email.com",
            password="Studentpass123",
            first_name="Student",
            last_name="User"
        )
        
        
    def test_create_student(self):
        student = Student.objects.create(
            user=self.student_user,
            birth_date=date(2008, 6, 1),
            class_teacher=self.teacher,
            note=4.5
        )
        
        self.assertEqual(student.user.email, "studentuser@email.com")
        self.assertEqual(student.birth_date, date(2008, 6, 1))
        self.assertEqual(student.class_teacher, self.teacher)
        self.assertEqual(student.note, 4.5)
        self.assertEqual(str(student), "Student User")
        
        
    def test_student_enrolled_courses(self):
        student = Student.objects.create(
            user=self.student_user,
            birth_date=date(2008, 6, 1),
            class_teacher=self.teacher,
            note=4.5
        )
        
        course1 = Course.objects.create(
            name="Calculus",
            code="MATH101",
            teacher=self.teacher,
            schedule="Mon-Wed-Fri 09:00-10:30"
        )
        
        course2 = Course.objects.create(
            name="Physics",
            code="PHYS101",
            teacher=self.teacher,
            schedule="Tue-Thu 11:00-12:30"
        )
        
        student.enrolled_course.add(course1, course2)
        
        self.assertIn(course1, student.enrolled_course.all())
        self.assertIn(course2, student.enrolled_course.all())
        self.assertEqual(student.enrolled_course.count(), 2)
        
        
        
#--------------------------------------------------------------------

# Serializers Tests

from rest_framework.test import APITestCase
from students.api.serializers import StudentSerializer, TeacherSerializer, CourseSerializer
from students.models import Student, Teacher, Course
from django.contrib.auth import get_user_model


User = get_user_model()


class StudentSerializerTest(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            email="studentuser@email.com",
            password="Studentpass123",
            first_name="Student",
            last_name="User"
        )
        
        
    def test_student_serializer(self):
        student = Student.objects.create(
            user=self.user,
            birth_date=date(2008, 6, 1),
            note=4.5
        )
        serializer = StudentSerializer(student)
        
        self.assertEqual(serializer.data["birth_date"], "2008-06-01")
        
        
        
class TeacherSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="teacheruser@email.com",
            password="Teacherpass123",
            first_name="Teacher",
            last_name="User"
        )
        
        
    def test_teacher_serializer(self):
        teacher = Teacher.objects.create(
            user=self.user,
            specialization="Mathematics"
        )
        
        serializer = TeacherSerializer(teacher)
        
        self.assertEqual(serializer.data["specialization"], "Mathematics")
        
        
        
class CourseSerializerTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="teacheruser@email.com",
            password="Teacherpass123",
            first_name="Teacher",
            last_name="User"
        )
        self.teacher = Teacher.objects.create(
            user=self.user,
            specialization="Mathematics"
        )
        
        
    def test_course_serializer(self):
        course = Course.objects.create(
            name="Calculus",
            code="MATH101",
            teacher=self.teacher,
            schedule="Mon-Wed-Fri 09:00-10:30"
        )
        
        serializer = CourseSerializer(course)
        
        self.assertEqual(serializer.data["name"], "Calculus")
        self.assertEqual(serializer.data["code"], "MATH101")
        
        
        
#--------------------------------------------------------------------

# Views Tests

from rest_framework.test import APITestCase
from django.urls import reverse
from students.models import Student, Teacher, Course
from django.contrib.auth import get_user_model
from rest_framework import status


User = get_user_model()


class StudentViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="studentuser@email.com",
            password="Studentpass123",
            first_name="Student",
            last_name="User"
        )
        self.client.login(email="studentuser@email.com", password="Studentpass123")
        
        
    def test_student_list_view(self):
        url = reverse("student-list")
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
        
class TeacherViewTest(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            email="teacheruser@email.com",
            password="Teacherpass123",
            first_name="Teacher",
            last_name="User"
        )
        self.client.login(email="teacheruser@email.com", password="Teacherpass123")

    def test_teacher_list(self):
        url = reverse("teacher-list")
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)