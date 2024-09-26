from django.contrib import admin

# Register your models here.
from .models import student

class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "studentid",
        "name",
        "gender",
        "photo",
    ]

admin.site.register(student,StudentAdmin)