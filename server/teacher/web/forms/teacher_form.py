from django import forms
# table Teacher
from ..models import Teacher

class TeacherForm(forms.ModelForm): 
    cpf = forms.CharField(widget=forms.TextInput(attrs={"data-mask": "000.000.000-00"}))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={"data-mask": "00000-000"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"data-mask": "(00) 00000-0000"}))
    
    class Meta: 
        model = Teacher
        # exclude = ("cod_ibge", )
        fields = "__all__"
    
    # Limpando cpf
    def clean_cpf(self): 
        cpf = self.cleaned_data["cpf"]
        return cpf.replace(".", "").replace("-", "")
    
    # Limpando ZipCode
    def clean_zip_code(self): 
        zip_code = self.cleaned_data["zip_code"]
        return zip_code.replace("-","")
    
    # Limpando phone
    def clean_phone(self): 
        phone = self.cleaned_data["phone"]
        return phone.replace("(", "").replace(")","").replace(" ","").replace("-", "")