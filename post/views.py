from multiprocessing import context
from django.shortcuts import render, redirect
from .models import BlogPost, Comment
from .forms import CommentForm, PostForm
from django.utils.text import slugify
from django.contrib import messages
# Create your views here.
def index(request):
    posts = BlogPost.objects.filter(show='PUB')
    context = {"posts": posts}
    return render(request, 'post/index.html', context)


def detail(request, slug):
    post = BlogPost.objects.get(slug = slug)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect('post:detail', slug=post.slug)
    context = {'post': post, "comments":comments, 'form':form }
    return render(request, 'post/detail.html', context)

def create_post(request):
    form = PostForm()
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post= form.save(commit=False)
            post.writer = request.user.userprofile
            post.slug = slugify(post.title)
            post.save()
            messages.success(request, "You have successfully created a blog post")
            return redirect("post:index")
    context = {"form": form}
    return render(request, "post/create_post.html", context)


def update_post(request, slug):
    
    profile = request.user.userprofile
    # 
    blog = BlogPost.objects.get(slug=slug)
    
    form = PostForm(instance=blog)
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            post= form.save(commit=False)
            post.writer = request.user.userprofile
            post.slug = slugify(post.title)
            post.save()
            messages.success(request, "You have successfully updated a blog post")
            return redirect("post:index")
    context = {"form": form}
    return render(request, "post/update_profile.html", context)

def delete_post(request, slug):
    
    blog = BlogPost.objects.get(slug=slug)
    
    if request.method == 'POST':
        blog.delete()
        messages.success(request, "Successfully deleted an article of yours")
        return redirect("myprofile:profile")
    
    context = {"blog":blog}
    return render(request, "post/delete_post.html", context)