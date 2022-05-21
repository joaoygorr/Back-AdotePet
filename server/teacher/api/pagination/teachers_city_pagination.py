from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class TeachersCityPagination(PageNumberPagination): 
    page_size = 6
    
    def get_paginated_response(self, data):
        return Response({
            'quantity-teachers': (self.page.paginator.count - self.page_size) if self.page.paginator.count > self.page_size else 0,
            'teachers': data
        })