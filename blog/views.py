from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    # Template Loader
    # blog/templates/blog/post_list.html
    return render(request, 'blog/post_list.html')


def post_detail(request, pk):
    return HttpResponse('post_detail: {}'.format(pk))
