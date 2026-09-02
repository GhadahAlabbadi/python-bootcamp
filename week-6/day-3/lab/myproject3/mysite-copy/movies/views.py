from django.shortcuts import render

movies = [
    {'id': 1, 'title': 'The Shawshank Redemption', 'year': 1994, 'rating': 9.3},
    {'id': 2, 'title': 'The Godfather', 'year': 1972, 'rating': 9.2},
    {'id': 3, 'title': 'The Dark Knight', 'year': 2008, 'rating': 9.0},
]

def movie_list(request):
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, id):
    movie = None
    for item in movies:
        if item['id'] == id:
            movie = item
            break
    return render(request, 'movies/movie_detail.html', {'movie': movie})