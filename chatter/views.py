from django.shortcuts import render
from blog.models import Post

# Create your views here.

def homepage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    return render(request, 'chatter/frontpage.html', {'posts': posts})

def about(request):
    return render(request, 'chatter/about.html')