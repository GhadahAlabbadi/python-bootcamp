from django.shortcuts import render
from django.http import Http404

# Mock course "database" — plain list of dicts, in-memory (no models/migrations).
courses = [
    {'id': 1, 'name': 'Python Basics', 'category': 'programming', 'difficulty': 'beginner',
     'instructor': 'Sarah Ahmed', 'syllabus': 'Variables, loops, functions, and basic data structures.'},
    {'id': 2, 'name': 'Django Fundamentals', 'category': 'web', 'difficulty': 'intermediate',
     'instructor': 'Omar Khalid', 'syllabus': 'Models, views, templates, URLs, and the ORM.'},
    {'id': 3, 'name': 'Advanced CSS', 'category': 'web', 'difficulty': 'advanced',
     'instructor': 'Lina Youssef', 'syllabus': 'Flexbox, Grid, animations, and responsive design.'},
    {'id': 4, 'name': 'Data Structures', 'category': 'programming', 'difficulty': 'intermediate',
     'instructor': 'Sarah Ahmed', 'syllabus': 'Lists, stacks, queues, trees, and hash maps.'},
    {'id': 5, 'name': 'Machine Learning Intro', 'category': 'data-science', 'difficulty': 'advanced',
     'instructor': 'Yusuf Al-Amin', 'syllabus': 'Regression, classification, and model evaluation.'},
    {'id': 6, 'name': 'SQL for Beginners', 'category': 'data-science', 'difficulty': 'beginner',
     'instructor': 'Lina Youssef', 'syllabus': 'SELECT, JOIN, GROUP BY, and basic schema design.'},
    {'id': 7, 'name': 'REST APIs with Django', 'category': 'web', 'difficulty': 'intermediate',
     'instructor': 'Omar Khalid', 'syllabus': 'Serializers, viewsets, authentication, and pagination.'},
]

PAGE_SIZE = 3

VALID_TABS = ('details', 'syllabus', 'instructor')


def course_list(request):
    category = request.GET.get('category', '').strip()
    difficulty = request.GET.get('difficulty', '').strip()
    query = request.GET.get('q', '').strip()

    filtered = courses
    if category:
        filtered = [c for c in filtered if c['category'] == category]
    if difficulty:
        filtered = [c for c in filtered if c['difficulty'] == difficulty]
    if query:
        filtered = [c for c in filtered if query.lower() in c['name'].lower()]

    # Step 8: basic pagination via ?page=
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    page = max(page, 1)

    total_pages = max(1, (len(filtered) + PAGE_SIZE - 1) // PAGE_SIZE)
    page = min(page, total_pages)

    start = (page - 1) * PAGE_SIZE
    page_courses = filtered[start:start + PAGE_SIZE]

    return render(request, 'courses/course_list.html', {
        'courses': page_courses,
        'category': category,
        'difficulty': difficulty,
        'query': query,
        'page': page,
        'total_pages': total_pages,
        'has_previous': page > 1,
        'has_next': page < total_pages,
    })


def course_detail(request, id):
    course = next((c for c in courses if c['id'] == id), None)
    if course is None:
        raise Http404('Course not found.')

    tab = request.GET.get('tab', 'details')
    if tab not in VALID_TABS:
        tab = 'details'

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'tab': tab,
    })