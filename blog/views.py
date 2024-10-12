import re
from django.shortcuts import render, redirect
from .models import PostModel, CommentPost
from .forms import PostForm, PostUpdateForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    post = PostModel.objects.all().order_by('-date')

    # this is the Post Form
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instence = form.save(commit=False)
            instence.author = request.user
            instence.save()
            return redirect('blog-index')
    else:
        form = PostForm()
   
    content = {
        'posts' : post,
        'form' : form,
    }
    return render(request, 'blog/index.html', content)

@login_required
def comment(request, pk):
    post = PostModel.objects.get(id=pk)
    # this is the Comment Form
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instence = c_form.save(commit=False)
            instence.user = request.user
            instence.post = post
            instence.save()
            return redirect('blog-comment', pk=post.id)
    else:
        c_form = CommentForm()
    context = {
        'post': post,
        'form': c_form,
    }   
    return render(request, 'blog/comment.html', context)

@login_required
def post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    # this is the Comment Form
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            instence = c_form.save(commit=False)
            instence.user = request.user
            instence.post = post
            instence.save()
            return redirect('post_detail', pk=post.id)
    else:
        c_form = CommentForm()
    context = {
        'post': post,
        'form': c_form,
    }
    return render(request, 'blog/post_detail.html', context)

@login_required
def post_edit(request, pk):
    form = PostUpdateForm()
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.id)
    else:
        form = PostUpdateForm(instance=post)
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/post_edit.html', context)

@login_required
def post_delete(request, pk):
    post = PostModel.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog-index')
    context = {
        'post': post,
    }
    return render(request, 'blog/post_delete.html', context)