from django.shortcuts import render, get_object_or_404,redirect
from .models import Student
from .forms import StudentForm

def student_list(request):
    query = request.GET.get('q', '')  # Get 'q' from URL, default ''
    
    if query:
        students = Student.objects.filter(
            full_name__icontains=query
        ) | Student.objects.filter(
            index_number__icontains=query
        )
    else:
        students = Student.objects.all()

    return render(request, 'students/student_list.html', {
        'students': students,
        'page_title': 'All Students',
        'query': query  # pass back to template for pre-filling
    })


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # index_number auto-generated
            return redirect('students:student_list')
    else:
        form = StudentForm()

    return render(request, 'students/student_form.html', {
        'form': form,
        'page_title': 'Add Student'
    })

def student_update(request, index_number):
    student = get_object_or_404(Student, index_number=index_number)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()  # preserves index_number
            return redirect('students:student_detail',index_number=student.index_number)
    else:
        form = StudentForm(instance=student)

    return render(request, 'students/student_form.html', {
        'form': form,
        'page_title': 'Update Student'
    })

def student_detail(request, index_number):
    student = get_object_or_404(Student, index_number=index_number)
    return render(request, 'students/student_detail.html', {
        'student': student,
        'page_title': student.full_name
    })

from django.contrib import messages  # Optional, for flash messages

def student_delete(request, index_number):
    student = get_object_or_404(Student, index_number=index_number)

    if request.method == "POST":
        student.delete()
        # Optional flash message
        messages.success(request, f"Student {student.full_name} deleted successfully.")
        return redirect('students:student_list')

    # GET request → show confirmation page
    return render(request, 'students/student_confirm_delete.html', {
        'student': student,
        'page_title': f"Delete {student.full_name}"
    })
