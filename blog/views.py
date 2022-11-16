from django.shortcuts import render
# Get data from the database
from .models import Post


# Create your views here.
def frontpage(request):
    # Get data from the database
    posts = Post.objects.all()
    return render(request, 'blog/frontpage.html', {'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/frontpage.html', {'post': post})
