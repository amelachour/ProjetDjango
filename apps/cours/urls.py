# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD
from . import views


from .views import add_course, course_list ,update_course ,delete_course

urlpatterns = [
    
  path('add/', add_course, name='add_course'),
  path('listcourses/', course_list, name='listcourses'),
  path('update/<int:pk>/', update_course, name='update_course'),
    path('delete/<int:pk>/', delete_course, name='delete_course'),

=======

from .views import add_course, course_list 

urlpatterns = [
    
      path('add/', add_course, name='add_course'),
    path('cours/', course_list, name='course_list'),

    
>>>>>>> c4f4019b0ff2ad6983f6bd24f6b5f3e4a8431bde
]


