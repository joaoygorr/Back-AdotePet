from rest_framework import serializers
from web.models import Teacher

class TeacherCitySerializer(serializers.ModelSerializer): 
    class Meta:
        model = Teacher
        fields = ('full_name', 'city', 'district', 'photo_user')