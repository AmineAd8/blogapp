from django.shortcuts import render, redirect
from .forms import SignUpForm
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-index')
    else:
        form = SignUpForm()
    content = {
        'form': form,
    }
    return render(request, 'users/sign_up.html', content)

@login_required
def profile(request):
    if request.method == 'POST':
        us_u = UserUpdateForm(request.POST, instance=request.user)
        p_u = ProfileUpdateForm(request.POST, request.FILES or None, instance=request.user.profilemodel)
        if us_u.is_valid() and p_u.is_valid():
            us_u.save()
            p_u.save()
            return redirect('users-profile')
    else:
        us_u = UserUpdateForm(instance=request.user)
        p_u = ProfileUpdateForm(instance=request.user.profilemodel)
    context = {
        'us_u' : us_u,
        'p_u' : p_u,
    }
    return render(request, 'users/profile.html', context)
