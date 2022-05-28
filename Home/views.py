from django.shortcuts import render, HttpResponse
from django.contrib import messages
from Home.models import Contect
from Blog.models import Post

# Create your views here.

def home(request):
    # return HttpResponse('This is Home')
    return render(request, 'home/home.html')

def contect(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        print(name, email, phone, content)
        
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contect = Contect(name = name, email = email, phone= phone, content = content)
            contect.save()
            messages.success(request, "Your message has been sent")
    return render(request, 'home/contect.html')

def about(request):
    # return HttpResponse('This is about')
    return render(request, 'home/about.html')


def search(request):
    query = request.GET['query']
    if len(query)>40:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count() ==0:
        messages.warning(request, "No search result found")
    params = {'allPosts' : allPosts, 'query': query}
    return render(request, 'home/search.html',params)