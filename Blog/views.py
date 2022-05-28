from django.shortcuts import render, HttpResponse
from Blog.models import Post
# Create your views here.


def blogHome(request):
    # return HttpResponse('This is blog home')
    allPosts = Post.objects.all()
    # print(allPosts)
    context = {'allPosts' : allPosts}
    return render(request, 'blog/blogHome.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'blog/blogPost.html',context)
