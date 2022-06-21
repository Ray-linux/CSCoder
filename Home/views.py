from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from Home.models import Contect
from Blog.models import Post
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

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
    return render(request, 'home/contact.html')

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

def login(request):
    return render(request, 'home/login.html')

def signup(request):
    return render(request, 'home/sign_up.html')


def handleSignup(request):
    if request.method =='POST':
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        
        if len(username) > 10:
            messages.success(request, "user must be eunder 15 charecters")
            return redirect('home')
        if not username.isalnum():
            messages.success(request, "user must onlu contain leters and number ")
            return redirect('home')
        if password != cpassword:
            messages.success(request, "passwords do not match")
            return redirect('home')
        
        # creat the user
        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect('/')
    else:
        return HttpResponse('404 -Not Found')
    
    
def handleLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "successfully logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credential, Please try again")
            return redirect('home')
    
        
    
def handleLogout(request):
    pass