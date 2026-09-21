from django.shortcuts import render

# In-memory data — same convention as the accounts app: no database model,
# just a plain Python list of dicts.
projects = [
    {'name': 'portfolio site', 'category': 'web', 'description': 'A personal portfolio built with Django.'},
    {'name': 'task tracker', 'category': 'web', 'description': 'A to-do list app with reminders.'},
    {'name': 'weather cli', 'category': 'tool', 'description': 'A command-line.'},
]


def home(request):
    return render(request, 'pages/home.html')


def about(request):
    return render(request, 'pages/about.html')


def project_list(request):
    category = request.GET.get('category', '')
    if category:
        filtered = [p for p in projects if p['category'] == category]
    else:
        filtered = projects
    return render(request, 'pages/projects.html', {
        'projects': filtered,
        'category': category,
    })