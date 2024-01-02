from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Post

def home(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'yourapp/login.html/', {'title': 'User Login'})

def register(request):
    return render(request, 'yourapp/register.html/', {'title': 'User Register'})
# def post(request):
#     return render(request, 'post.html')

def post(request):
    if request.method == 'POST':
        # Save data to the database
        name = request.POST['name']
        desc = request.POST['desc']
        image = request.FILES['file'].name
        post = Post(name=name, desc=desc, image=image)
        post.save()
        return redirect('post')  # Redirect to the same page to display all posts

    # Retrieve all posts from the database
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'yourapp/post.html/', {'posts': posts})
