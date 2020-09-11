from pickle import GET

from django.shortcuts import render
from .models import Post, Register


def createpost(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post = Post()
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.save()

            return render(request, 'createpost.html')

    else:
        return render(request, 'createpost.html')

