from django.shortcuts import render, HttpResponse
from .models import Post

def main(request):
    data = Post.objects.all()
    post_list = {'posts': data}
    return render(request, 'index.html', context=post_list)

def post(request, pk):
    data = Post.objects.get(id=pk)
    text = {'post': data, 'id': str(pk)}
    return render(request, 'post.html', context=text)

def about(request):
    return render(request, 'about.html')