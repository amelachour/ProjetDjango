from django.shortcuts import render, redirect
from .forms import CourseForm
from .models import Cours
from django.contrib.auth.decorators import login_required



def course_list(request):
    courses = Cours.objects.all()
    return render(request, "courses\course_list.html", {"courses": courses})


def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, "courses/add_course.html", {"form": form})


