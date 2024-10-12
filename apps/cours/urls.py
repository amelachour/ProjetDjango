# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import add_course, course_list 

urlpatterns = [
    
      path('add/', add_course, name='add_course'),
    path('cours/', course_list, name='course_list'),

    
]


