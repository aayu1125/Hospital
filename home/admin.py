from django.contrib import admin
from .models import Department, Doctor

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'uuid', 'created_at', 'updated_at') 
    search_fields = ('name', )
    ordering = ('name', )

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'uuid', 'created_at', 'updated_at', 'department') 
    search_fields = ('name', )
    ordering = ('name', )