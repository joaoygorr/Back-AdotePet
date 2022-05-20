from django import forms
import json
# table Teacher
from ..models import Teacher
from ..services import zip_code_service

class TeacherForm(forms.ModelForm): 
    cpf = forms.CharField(widget=forms.TextInput(attrs={"data-mask": "000.000.000-00"}))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={"data-mask": "00000-000"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"data-mask": "(00) 00000-0000"}))
    
    class Meta: 
        model = Teacher
        exclude = ("cod_ibge", )
    
    # Limpando cpf
    def clean_cpf(self): 
        cpf = self.cleaned_data["cpf"]
        return cpf.replace(".", "").replace("-", "")
    
    # Limpando ZipCode
    def clean_zip_code(self): 
        zip_code = self.cleaned_data["zip_code"]
        zip_code_formated = zip_code.replace("-","")
        response = zip_code_service.search_city_zip_Code(zip_code_formated)
        if response.status_code == 400:
            raise forms.ValidationError("The zip code entered is incorrect! ")
        city_api = json.loads(response.content)
        if "erro" in city_api: 
            raise forms.ValidationError("The specified zip code was not found.")
        return zip_code.replace("-","")
    
    # Limpando phone
    def clean_phone(self): 
        phone = self.cleaned_data["phone"]
        return phone.replace("(", "").replace(")","").replace(" ","").replace("-", "")
    
    def save(self, commit=True): 
        instance = super(TeacherForm, self).save(commit=False)
        response = zip_code_service.search_city_zip_Code(self.cleaned_data.get('zip_code'))
        city_api = json.loads(response.content)
        instance.cod_ibge = city_api["ibge"]
        instance.save()
        return instance