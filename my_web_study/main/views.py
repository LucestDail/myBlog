from django.shortcuts import render, redirect
from .models import Post
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def blog(request):
    postlist = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist': postlist})


def posting(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'post': post})


def new_post(request):
    if request.method == 'POST':
        new_article = Post.objects.create(
            writer=request.POST['writer'],
            title=request.POST['title'],
            contents=request.POST['contents'],
        )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')


def remove_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/blog/')
    return render(request, 'main/remove_post.html', {'Post': post})


def update_post(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.title = request.POST['writer']
        post.contents = request.POST['contents']
        post.writer = request.POST['writer']
        post.save()
        return redirect('/blog/')
    return render(request, 'main/update_post.html')