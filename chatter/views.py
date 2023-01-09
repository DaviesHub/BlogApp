from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'chatter/frontpage.html')

def about(request):
    return render(request, 'chatter/about.html')