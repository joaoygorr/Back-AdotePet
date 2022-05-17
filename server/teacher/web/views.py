from django.shortcuts import redirect, render
from .models import Teacher
# import form teacher
from .forms import teacher_form

# Create your views here.
# Cadastro
def register_teacher(request): 
    if request.method == "POST": 
        form_teacher = teacher_form.TeacherForm(request.POST, request.FILES)
        if form_teacher.is_valid(): 
            form_teacher.save()
            return redirect('list_teachers')
    else: 
        form_teacher = teacher_form.TeacherForm()
    return render(request, 'form_teacher.html', {'form_teacher': form_teacher})

# Listando Teacher
def list_teachers(request): 
    teachers = Teacher.objects.all()
    return render(request, 'list_teachers.html', {'teachers': teachers})