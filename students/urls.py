from django.urls import path
from . import views


urlpatterns =[
    path('create/',views.create_student,name='create_student'),
    path('success/',views.success_view,name='success'),
    path('list/', views.student_list, name='student_list'),
]