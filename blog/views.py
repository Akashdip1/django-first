from django.shortcuts import render
from .models import Post 


def home(request):

    #An optional dictionary of data to be passed to the template.
    context =  {
        'posts' : Post.objects.all(),
        'title' : 'Home'
    }   

    return render(request, 'blog/home.html', context)

def about(request):
    
    return render(request, 'blog/about.html', {'title' : 'About'})

