from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_settings, name=""),
    path('exam_timer', views.exam_timer, name="exam_timer"),
    path('exam_list', views.exam_list, name="exam_list")
]