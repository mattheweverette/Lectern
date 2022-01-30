from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from summarizer.models import Lecture


def register(request):
    if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                form.save()
                messages.success(request, f'Account created for {username}!')
                return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def profile(request):
    user_posts = Lecture.objects.filter(poster=request.user)
    return render(request, 'profile.html', {'posts': user_posts})