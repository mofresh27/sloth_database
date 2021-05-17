from django.contrib import admin
from .models import School, Student, Department, Certificate, Grade, Faculty

# Register your models here.
admin.site.register(School)
admin.site.register(Faculty)
admin.site.register(Certificate)
admin.site.register(Grade)
admin.site.register(Student)
admin.site.register(Department)