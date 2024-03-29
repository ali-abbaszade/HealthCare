from django.shortcuts import render, get_object_or_404

from blog.forms import CommentForm
from .models import Category, Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q


def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1)

    if kwargs.get("tag_name"):
        posts = posts.filter(tags__name__in=[kwargs["tag_name"]])

    if kwargs.get("cat_name"):
        posts = posts.filter(category__name=kwargs["cat_name"])

    page = request.GET.get("page", 1)
    paginator = Paginator(posts, 3)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {"posts": posts}
    return render(request, "blog/blog-sidebar.html", context)


def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your comment submited successfuly")
        else:
            messages.error(request, "Your comment didnt submited")

    form = CommentForm()
    comments = Comment.objects.filter(post=post.id, approved=True)

    context = {"post": post, "form": form, "comments": comments}
    return render(request, "blog/blog-single.html", context)


def blog_search(request):
    search_query = ""
    if request.GET.get("s"):
        search_query = request.GET.get("s")

    posts = Post.objects.filter(
        Q(content__icontains=search_query) | Q(title__icontains=search_query)
    )

    context = {"posts": posts}
    return render(request, "blog/blog-sidebar.html", context)
