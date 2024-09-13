from django.urls import path
from students.api import views

urlpatterns = [
    path("teachers/", views.TeacherListCreateAPIView.as_view(), name="teacher-list"),
    path("teachers/<int:pk>/", views.TeacherDetailAPIView.as_view(), name="teacher-detail"),
    path("courses/", views.CourseListCreateAPIView.as_view(), name="course-list"),
    path("courses/<int:pk>/", views.CourseDetailAPIView.as_view(), name="course-detail"),
    path("students/", views.StudentListCreateAPIView.as_view(), name="student-list"),
    path("students/<int:pk>/", views.StudentDetailAPIView.as_view(), name="student-detail"),
]