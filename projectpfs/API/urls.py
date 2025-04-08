from django.urls import path
from .views import StudentList

urlpatterns = [
    path('students/', StudentList.as_view(), name='student_list'),
]