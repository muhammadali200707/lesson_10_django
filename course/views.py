from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Speciality
from .forms import CourseForm, CourseUpdateForm
from django.http import HttpRequest


def courses_list_view(request):
    courses = Course.objects.all()
    specialitys = Speciality.objects.all()
    context = {
        "courses": courses,
        "specialitys": specialitys,
    }
    return render(request, 'course.html', context)


def course_detail_view(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'course_detail.html', {"course": course})


def course_create_view(request):
    if request.method == "POST":
        form = CourseForm(data=request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.image = request.POST['image']
            course.save()
            return redirect('course-list')
    form = CourseForm()
    return render(request, 'course_create.html', {'form': form})


def course_update_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseUpdateForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course-detail', pk=course.pk)
        else:
            if course.rating < 0 or course.rating > 5:
                form = CourseUpdateForm()
                return render(request, 'course_update.html', {'form': form, "message_error": "Something went wrong!", "course": course})
    course = Course.objects.get(pk=pk)
    return render(request, 'course_update.html', {"course": course})


def course_delete_view(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('course-list')
