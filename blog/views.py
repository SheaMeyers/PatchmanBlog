from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.filter(is_published=True).order_by('created_date')
    return render(request, 'post_list.html', {'posts': posts})