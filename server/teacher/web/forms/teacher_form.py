from django import forms
# table Teacher
from ..models import Teacher

class TeacherForm(forms.ModelForm): 
    class Meta: 
        model = Teacher
        fields = "__all__"