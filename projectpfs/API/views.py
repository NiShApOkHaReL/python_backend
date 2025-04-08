from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.generics import ListAPIView
from .pagination import StudentPagination
from rest_framework import filters, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# Create your views here.
class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StudentPagination #For pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]       #For filter operation
    filterset_fields = ['prog','department']
    search_fields =['name','prog']
    # search_fields =['^name']



# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
# from django_filters import rest_framework as filters
# from rest_framework.pagination import PageNumberPagination
# from .models import Student
# from .serializers import StudentSerializer
# from .pagination import StudentPagination  # your custom pagination

# class StudentList(APIView):
#     def get(self, request, format=None):
#         students = Student.objects.all()

#         # FILTERING
#         prog = request.GET.get('prog')
#         department = request.GET.get('department')

#         if prog:
#             students = students.filter(prog=prog)
#         if department:
#             students = students.filter(department=department)

#         # SEARCH
#         search_query = request.GET.get('search')
#         if search_query:
#             students = students.filter(
#                 models.Q(name__icontains=search_query) |
#                 models.Q(prog__icontains=search_query)
#             )

#         # PAGINATION
#         paginator = StudentPagination()
#         paginated_students = paginator.paginate_queryset(students, request)

#         serializer = StudentSerializer(paginated_students, many=True)
#         return paginator.get_paginated_response(serializer.data)
