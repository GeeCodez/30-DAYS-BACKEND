import json
from django.http import JsonResponse
from django.views import View
from .models import Student

class StudentListCreateView(View):
    def get(self, request):
        students = list(Student.objects.values())
        return JsonResponse({"students": students}, status=200)

    def post(self, request):
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        student = Student.objects.create(**data)
        return JsonResponse({
            "message": "Student created successfully",
            "index_number": student.index_number
        }, status=201)


class StudentDetailView(View):
    def get(self, request, index_number):
        try:
            student = Student.objects.get(index_number=index_number)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)

        return JsonResponse({
            "student": {
                "index_number": student.index_number,
                "name": student.full_name,
                "age": student.age
            }
        }, status=200)

    def put(self, request, index_number):
        try:
            student = Student.objects.get(index_number=index_number)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)

        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        for field, value in data.items():
            setattr(student, field, value)

        student.save()

        return JsonResponse({"message": "Student updated successfully"}, status=200)

    def delete(self, request, index_number):
        try:
            student = Student.objects.get(index_number=index_number)
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)

        student.delete()
        return JsonResponse({"message": "Student deleted successfully"}, status=200)
