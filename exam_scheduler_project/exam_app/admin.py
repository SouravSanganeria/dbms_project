from django.contrib import admin
from exam_app.models import Course,Dept,Slot,Student,Faculty,Exam,Exam_faculty,Exam_student,Room
# Register your models here.

class HiddenModelAdmin(admin.ModelAdmin):
    def get_model_perms(self, *args, **kwargs):
        perms = admin.ModelAdmin.get_model_perms(self, *args, **kwargs)
        perms['list_hide'] = True
        return perms

admin.site.register(Course)
admin.site.register(Dept)
admin.site.register(Slot)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Exam)
admin.site.register(Exam_faculty)
admin.site.register(Exam_student)
admin.site.register(Room)
