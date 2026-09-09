import os
from PIL import Image, UnidentifiedImageError
from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect

ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png'}

posts = []


def feed(request):
    error = None

    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        description = request.POST.get('description', '').strip()
        image_file = request.FILES.get('image')

        if not username or not image_file:
            error = 'Username and an image are both required.'
        else:
            ext = os.path.splitext(image_file.name)[1].lower()
            if ext not in ALLOWED_EXTENSIONS:
                error = 'Only .jpg, .jpeg, and .png files are allowed.'
            else:

                try:
                    Image.open(image_file).verify()
                except (UnidentifiedImageError, OSError):
                    error = 'That file is not a valid image.'

        if not error:
            image_file.seek(0)  
            saved_path = default_storage.save(f'posts/{image_file.name}', image_file)
            posts.append({
                'id': len(posts) + 1,
                'username': username,
                'description': description,
                'image_url': settings.MEDIA_URL + saved_path,
                'likes': 0,
            })
            return redirect('posts:feed')

    return render(request, 'posts/feed.html', {
        'posts': list(reversed(posts)), 
        'error': error,
    })


def like_post(request, post_id):
    for post in posts:
        if post['id'] == post_id:
            post['likes'] += 1
            break
    return redirect('posts:feed')