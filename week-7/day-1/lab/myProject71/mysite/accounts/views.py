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
        return render(request, 'accounts/profile.html', {'username': username})

def status(request):
    username = request.session.get('username')
    return JsonResponse({
        'logged_in': bool(username),
        'username': username,
    })