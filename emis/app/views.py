from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from . models import Exam, models
from . forms import ExamForm
from django.utils import timezone

def exam_timer(request, exam_id):

    exam = get_object_or_404(Exam, pk=exam_id)
    context = {'exam' : exam}

    return render(request, 'app/exam_timer.html', context=context)

def create_exam(request):

    form = ExamForm(request.POST)

    if request.method=='POST':

        if form.is_valid():
            
            form.save()
            return redirect('')
        
        else:
            form = ExamForm()

    context = { 'form' : form }

    return render(request, 'app/create_exam.html', context=context)

def exam_list(request):

    exams = Exam.objects.order_by('-start_time')[:20]
    context = { 'exams' : exams}

    return render(request, 'app/exam_list.html', context=context)
