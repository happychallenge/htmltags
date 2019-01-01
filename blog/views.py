from django.shortcuts import render, redirect

from .models import Post
from .forms import PostForm

# Create your views here.
def post_add(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect(post)

    else:
        form = PostForm()

    context = { 'form': form }
    return render(request, 'blog/post_add.html', context)


def post_edit(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect(post)

    else:
        form = PostForm(instance=post)

    context = { 'form': form }
    return render(request, 'blog/post_edit.html', context)


def post_list(request):
    post_list = Post.objects.all()
    context = { 'post_list': post_list }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, id):
    post = Post.objects.all()[:2]

    context = { 'last': post[0], 'before': post[1] }
    return render(request, 'blog/post_detail.html', context)