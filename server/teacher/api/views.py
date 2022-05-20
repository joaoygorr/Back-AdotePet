from django.shortcuts import render
from rest_framework.views import Response
from rest_framework.views import APIView
from .service.city_attendance_service import list_teachers_city
from .serializer import teachers_city_serializer

# Create your views here.

class TeachersCityList(APIView): 
    def get(self, request, format=None): 
        zip_code = self.request.query_params.get('zip_code', None)
        teachers = list_teachers_city(zip_code)
        serializer = teachers_city_serializer.TeacherCitySerializer(teachers, many=True, context={"request": request})
        
        return Response(serializer.data)