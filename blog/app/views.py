from django.shortcuts import render, HttpResponse
from .models import Post

def main(request):
    post = Post.objects.get(id=1)
    print("Attributes: " + str(post.__dict__))
    print("post: " + str(post))
    print('content: ' + str(post.content))
    data = {"txt": post.content,}
    return render(request, 'index.html', context=data)