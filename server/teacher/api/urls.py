from django.urls import path
from .views import TeachersCityList

urlpatterns = [
    path("teachers-city", TeachersCityList.as_view(), name='teachers-city-list'),
]
