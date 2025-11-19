from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'index_number', 'email', 'age', 'is_active', 'date_created')
    list_filter = ('is_active', 'date_created')
    search_fields = ('full_name', 'email', 'index_number')
    ordering = ('full_name',)
