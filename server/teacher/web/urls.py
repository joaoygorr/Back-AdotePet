from django.urls import path
from .views import register_teacher, list_teachers

urlpatterns = [
    path('register_teacher', register_teacher, name='register_teacher'),    
    path('list_teachers', list_teachers, name='list_teachers')    
]
