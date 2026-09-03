from django.http import Http404
from django.shortcuts import render

courses = [
    {
        'id': 1,
        'slug': 'django-basics',
        'title': 'Django Basics',
        'category': 'backend',
    },
    {
        'id': 2,
        'slug': 'react-fundamentals',
        'title': 'React Fundamentals',
        'category': 'frontend',
    },
    {
        'id': 3,
        'slug': 'devops-101',
        'title': 'DevOps 101',
        'category': 'infrastructure',
    },
]

def course_list(request):
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_category(request, category):
    filtered = [c for c in courses if c['category'] == category]
    return render(request, 'courses/course_category.html', {'courses': filtered, 'category': category})

def course_detail(request, slug):
    for course in courses:
        if course['slug'] == slug:
            return render(request, 'courses/course_detail.html', {'course': course})
    raise Http404('Course does not exist')