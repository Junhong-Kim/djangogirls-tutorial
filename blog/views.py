from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post


def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('published_date')
    # Template Loader
    # blog/templates/blog/post_list.html
    return render(request, 'blog/post_list.html', {
        'posts': posts,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })
    return HttpResponse('post_detail: {}'.format(pk))
