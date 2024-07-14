from django.urls import path
from . import views

urlpatterns = [
    path('create_exam/', views.create_exam, name="create_exam"),
    path('exam/<int:exam_id>/', views.exam_timer, name="exam_timer"),
    path('', views.exam_list, name="")
]