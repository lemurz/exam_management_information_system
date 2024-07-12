from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from . models import Exam, models
from . forms import ExamForm
import datetime

def exam_timer(request, exam_id):

    exam = get_object_or_404(Exam, pk=exam_id)
    context = {'exam' : exam}
    return render(request, 'app/exam_timer.html', context=context)

def exam_settings(request):

    form = ExamForm(request.POST)

    if request.method=='POST':

        if form.is_valid():
            form.save()
        else:
            form = ExamForm()

    context = { 'form' : form }

    return render(request, 'app/index.html', context=context)

def exam_list(request):

    forms = Exam.objects.all()
    context = { 'forms' : forms }

    return render(request, 'app/exam_list.html', context=context)
