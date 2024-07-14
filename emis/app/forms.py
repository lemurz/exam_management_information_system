from django import forms
from . models import Exam

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = [ 'course_name', 'course_code', 'start_time', 'end_time', 'no_leave_start', 'no_leave_end' ]
        widgets = {
            'course_name' : forms.TextInput(attrs={'class' : 'form-control' }),
            'course_code' : forms.TextInput(attrs={'class' : 'form-control'}),
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'no_leave_start': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 00:30:00 for 30 minutes'}),
            'no_leave_end': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. 00:30:00 for 30 minutes'})
            
            }
