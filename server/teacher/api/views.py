from django.shortcuts import render
from rest_framework.views import Response
from rest_framework.views import APIView
from .service.city_attendance_service import list_teachers_city
from .serializer import teachers_city_serializer
from .pagination import teachers_city_pagination
# Create your views here.

class TeachersCityList(APIView, teachers_city_pagination.TeachersCityPagination): 
    def get(self, request, format=None): 
        zip_code = self.request.query_params.get('zip_code', None)
        teachers = list_teachers_city(zip_code)
        result = self.paginate_queryset(teachers, request)
        serializer = teachers_city_serializer.TeacherCitySerializer(result, many=True, context={"request": request})
        
        return self.get_paginated_response(serializer.data)