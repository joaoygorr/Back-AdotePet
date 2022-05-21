from web.services import zip_code_service
from web.models import Teacher
from rest_framework import serializers
import json

def list_teachers_city(zip_code): 
    cod_ibge = search_city_zip_code(zip_code)['ibge']
    try: 
        teachers = Teacher.objects.filter(cod_ibge=cod_ibge).order_by("id")
        return teachers
    except Teacher.DoesNotExist:
        return []

def search_city_zip_code(zip_code): 
    response = zip_code_service.search_city_zip_Code(zip_code)
    if response.status_code == 400: 
        raise serializers.ValidationError("The zip code entered is incorrect!")
    city_api = json.loads(response.content)
    if "erro" in city_api:
        raise serializers.ValidationError("The specified zip code was not found.")
    return city_api