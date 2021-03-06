from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm


# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserLoginForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                remember = form.cleaned_data.get('remember_me')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    if not remember:
                        request.session.set_expiry(0)
                    return redirect('/')
            else:
                return render(request, 'accounts/login.html', {'form': form})
        else:
            form = UserLoginForm()
            context = {'form': form}
            return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')


@login_required(login_url='/accounts/login')
def logout_view(request):
    logout(request)
    return redirect('/')


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')
