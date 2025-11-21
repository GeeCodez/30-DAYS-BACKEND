from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return HttpResponse("Student app is working ")

def list_students(request):
    students=Student.objects.all().values()
    return JsonResponse(list(students), safe=False)

from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        student = Student.objects.create(
            full_name=data.get('full_name'),
            age=data.get('age'),
            email=data.get('email')
        )

        return JsonResponse({
            "message": "Student created successfully",
            "index_number": student.index_number
        })

    return JsonResponse({"error": "Only POST allowed"}, status=400)

@csrf_exempt
def update_student(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        index_number = data.get('index_number')
        if not index_number:
            return JsonResponse({"error": "index_number is required"}, status=400)

        try:
            student = Student.objects.get(index_number=index_number)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)

        # Update fields if present
        if 'full_name' in data:
            student.full_name = data['full_name']
        if 'age' in data:
            student.age = data['age']
        if 'email' in data:
            student.email = data['email']

        student.save()

        return JsonResponse({
            "message": "Student updated successfully",
            "index_number": student.index_number
        })

    return JsonResponse({"error": "Only POST allowed"}, status=400)

@csrf_exempt
def delete_student(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        index_number = data.get('index_number')
        if not index_number:
            return JsonResponse({"error": "index_number is required"}, status=400)

        try:
            student = Student.objects.get(index_number=index_number)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)

        student.delete()

        return JsonResponse({
            "message": "Student deleted successfully",
            "index_number": index_number
        })

    return JsonResponse({"error": "Only POST allowed"}, status=400)
