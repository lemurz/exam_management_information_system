from django.db import models
from django import forms
from django.utils import timezone

class ExamLog(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    student_count = models.CharField(max_length=100)
    additional_details = models.TextField(max_length=100)
    log_time = timezone.now()

    class Meta:
        verbose_name_plural = 'Exam Logs'

class Exam(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    no_leave_start = models.DurationField()
    no_leave_end = models.DurationField()


