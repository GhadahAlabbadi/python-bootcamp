from django.http import Http404
from django.shortcuts import render

posts = [
    {
        'id': 1,
        'title': 'Getting Started with Django',
        'category': 'django',
        'content': 'Django is a high-level Python web framework that encourages rapid development.',
    },
    {
        'id': 2,
        'title': 'Understanding URL Routing',
        'category': 'django',
        'content': 'URL routing maps incoming request paths to the view functions that handle them.',
    },
    {
        'id': 3,
        'title': 'Why I Love Python',
        'category': 'python',
        'content': 'Python is known for its readability and its huge ecosystem of libraries.',
    },
]

def post_list(request):
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):
    for post in posts:
        if post['id'] == id:
            return render(request, 'blog/post_detail.html', {'post': post})
    raise Http404('Post does not exist')

def post_category(request, category):
    filtered = [post for post in posts if post['category'] == category]
    return render(request, 'blog/post_category.html', {'posts': filtered, 'category': category})