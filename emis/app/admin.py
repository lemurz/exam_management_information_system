from django.contrib import admin
from . models import ExamLog

# Register your models here.
admin.site.site_header = 'LSBU Invigilator Portal'

class ExamLogAdmin(admin.ModelAdmin):

    list_display = ['course_name', 'course_code', 'student_count', 'log_time']
    search_fields = ('course_name', 'course_code', 'student_count', 'additional_details')

admin.site.register(ExamLog, ExamLogAdmin)