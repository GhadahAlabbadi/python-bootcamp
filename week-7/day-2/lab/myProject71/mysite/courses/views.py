from django.shortcuts import render
from django.http import Http404

courses = [
    {
        'slug': 'python-basics',
        'name': 'python basics',
        'level': 'Beginner',
        'students': 24,
        'description': '<script>An introduction to Python syntax and core programming '
                        'concepts, built for absolute beginners.</script>',
        'image': 'images/python.png',
    },
    {
        'slug': 'django-fundamentals',
        'name': 'django fundamentals',
        'level': 'Intermediate',
        'students': 12,
        'description': 'Learn how to build full web applications with Django: '
                        'models, views, templates, and the ORM, all explained '
                        'through hands-on projects.',
        'image': 'images/django.jpg',
    },
    {
        'slug': 'advanced-css',
        'name': 'advanced css',
        'level': 'Advanced',
        'students': 0,
        'description': 'A deep dive into modern CSS layout: Flexbox, Grid, and custom properties. ',
        'image': 'images/css.png',
    },
]


def home(request):
    return render(request, 'courses/home.html', {'username': 'ghadah'})


def course_list(request):
    level = request.GET.get('level', '')
    if level:
        filtered = [c for c in courses if c['level'].lower() == level.lower()]
    else:
        filtered = courses
    return render(request, 'courses/courses.html', {
        'username': 'ghadah',
        'courses': filtered,
        'level': level,
    })


def course_detail(request, slug):
    for course in courses:
        if course['slug'] == slug:
            return render(request, 'courses/course_detail.html', {
                'username': 'ghadah',
                'course': course,
            })
    raise Http404('Course not found.')