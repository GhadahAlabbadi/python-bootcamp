from PIL import Image, UnidentifiedImageError
from django.conf import settings
from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse

accounts = []

class RegisterView(View):
    def get(self, request):
        return render(request, 'accounts/register.html')

    def post(self, request):
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        if not username or not password:
            return render(request, 'accounts/register.html', {
                'error': 'Username and password are both required.'
            })
        if any(a['username'] == username for a in accounts):
            return render(request, 'accounts/register.html', {
                'error': 'That username is already taken.'
            })
        accounts.append({'username': username, 'password': password})
        return render(request, 'accounts/register.html', {
            'success': f'Account "{username}" created. You can log in now.'
        })


class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        match = next(
            (a for a in accounts if a['username'] == username and a['password'] == password),
            None,
        )
        if match is None:
            return render(request, 'accounts/login.html', {
                'error': 'Incorrect username or password.'
            })
        request.session['username'] = username
        return redirect('accounts:profile')


class ProfileView(View):
    def get(self, request):
        username = request.session.get('username')
        if not username:
            return redirect('accounts:login')

        account = next((a for a in accounts if a['username'] == username), None)
        avatar_path = account.get('avatar') if account else None
        avatar_url = settings.MEDIA_URL + avatar_path if avatar_path else None

        return render(request, 'accounts/profile.html', {
            'username': username,
            'avatar_url': avatar_url,
        })


def upload_avatar(request):
    username = request.session.get('username')
    if not username:
        return redirect('accounts:login')

    account = next((a for a in accounts if a['username'] == username), None)
    if account is None:
        return redirect('accounts:login')

    if request.method != 'POST':
        return render(request, 'accounts/upload_avatar.html')

    avatar_file = request.FILES.get('avatar')
    if not avatar_file:
        return render(request, 'accounts/upload_avatar.html', {
            'error': 'Please choose an image file to upload.'
        })
    
    try:
        Image.open(avatar_file).verify()
    except (UnidentifiedImageError, OSError):
        return render(request, 'accounts/upload_avatar.html', {
            'error': 'That file is not a valid image.'
        })
    avatar_file.seek(0)
    
    saved_path = default_storage.save(f'avatars/{username}_{avatar_file.name}', avatar_file)
    account['avatar'] = saved_path

    return redirect('accounts:profile')


def status(request):
    username = request.session.get('username')
    return JsonResponse({
        'logged_in': bool(username),
        'username': username,
    })