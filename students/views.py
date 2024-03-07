from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def student_list(request):
    students = Student.objects.all()
    enumerated_students = [(index + 1, student) for index, student in enumerate(students)]
    return render(request, 'student_list.html', {'enumerated_students': enumerated_students})
