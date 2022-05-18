from django.urls import path
from .views import register_teacher, list_teachers, edit_teacher, remove_teacher

urlpatterns = [
    path('register_teacher', register_teacher, name='register_teacher'),    
    path('list_teachers', list_teachers, name='list_teachers'),
    path('edit_teacher/<int:teacher_id>', edit_teacher, name='edit_teacher'),
    path("remove_teacher/<int:teacher_id>", remove_teacher, name='remove_teacher')
]
