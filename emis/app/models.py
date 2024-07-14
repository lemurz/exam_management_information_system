from django.db import models
from django import forms
from django.utils import timezone

class ExamLog(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    student_count = models.CharField(max_length=100)
    additional_details = models.TextField(max_length=100)
    log_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Exam Logs'

    def save(self, *args, **kwargs):

        local_time = timezone.localtime(timezone.now())
        self.log_time = local_time
        super().save(*args, **kwargs)

class Exam(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    no_leave_start = models.DurationField()
    no_leave_end = models.DurationField()



