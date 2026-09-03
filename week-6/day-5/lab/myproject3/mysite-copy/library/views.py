from django.http import Http404
from django.shortcuts import render

books = [
    {
        'id': 1,
        'title': 'Welcome to Django',
        'author': 'Ghadah',
        'year': 2026
    },
    {
        'id': 2,
        'title': 'FastAPI demystified',
        'author': 'Majd',
        'year': 2026
    },
]

def book_list(request):
    context = {'books': books}
    return render(request, 'library/book_list.html', context)

def book_detail(request, id):
    for book in books:
        if book['id'] == id:
            return render(request, 'library/book_detail.html', book)
    raise Http404('Book does not exist')