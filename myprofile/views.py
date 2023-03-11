import profile
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from post.models import BlogPost

from .models import UserProfile
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from .forms import ProfileForm

# Create your views here.
def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Congratulations, you just created a new account!")
            return redirect("myprofile:signin")
        else:
            messages.warning(request, form.errors)
            return redirect("myprofile:create")
    context = {"form":form}
    return render(request, "myprofile/register.html", context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("myprofile:update_profile")
        
        else:
            messages.info(request, "Invalid credential")
            return redirect("myprofile:signin")
        
    context = {}
    return render(request, "myprofile/login.html", context)

def signout(request):
    logout(request)
    return redirect("post:index")

def update_profile(request):
    profile = UserProfile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "You successfully updated your profile")
            return redirect("post:index")

        else:
            messages.info(request, form.errors)
            
            
        
    context = {"form":form}
    return render(request, "myprofile/update_profile.html", context)


def user_profile(request):
    profile = request.user.userprofile
    blogs = BlogPost.objects.filter(writer=profile)
    context = {"profile":profile, "blogs":blogs}
    return render(request, "myprofile/profile.html", context)