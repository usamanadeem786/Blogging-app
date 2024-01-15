from django.shortcuts import render , redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Post, Comment, Like
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as authorize, logout as deauth

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

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Check if the user is the author of the post
    if request.method == 'POST' and request.user.is_authenticated:
        post.delete()

    return redirect('/post/')  # Replace with the URL name for your all posts page

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user.is_authenticated:
        # Authenticated user
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            messages.info(request, 'You have already liked this post.')
        else:
            messages.success(request, 'You have successfully liked the post.')
    else:
        messages.warning(request, 'Please log in to like the post.')
    post.refresh_from_db()

    return redirect('/post/', post_id=post_id)  # Replace 'your_redirect_url' with the appropriate URL

@login_required
def delete_comment(request, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=comment_id)

        # Check if the user has permission to delete the comment
        if comment.user != request.user:
            # User does not have permission to delete this comment
            return HttpResponseBadRequest("You do not have permission to delete this comment.")

        # Delete the comment
        comment.delete()

        # Redirect to the post detail page after deleting the comment
        return redirect('post')
    else:
        messages.error(request, 'You Need to Login First')
        return redirect('/login/')

def comment_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST' and request.user.is_authenticated:
        comment_text = request.POST.get('comment')

        # Create a new comment instance
        comment = Comment(user=request.user, post=post, text=comment_text)
        comment.save()
    else:
        messages.warning(request, 'For Comment this post You need to Login First')

    return redirect('/post/')  # Replace 'your_redirect_url' with the appropriate URL

def login(request):
    if(request.method == 'POST'):
        form = AuthenticationForm()
        uname = request.POST['username']
        upass = request.POST['password']
        user = authenticate(username=uname, password=upass)
        if user is None:
            messages.error(request, 'Username and Password are not Correct')
            return redirect('/login/')
        else:
            authorize(request, user)
            return redirect('/post/')
    else:
        if(request.user is None):
            return redirect('/post/')
        form = AuthenticationForm()
    return render(request, 'yourapp/login.html/', {'title': 'User Login', 'form': form})

def logout(request):
    if request.user.is_authenticated:
        deauth(request)
        messages.success(request, 'You have Successfully Logout')
    return redirect('/login/')

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form =  UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'User Successfully Register')
            return redirect('login')
    return render(request, 'yourapp/register.html/', {'title': 'User Register', 'form': form})

def post(request):
    if request.method == 'POST' and request.user.is_authenticated:
        # Save data to the database
        name = request.POST['name']
        desc = request.POST['desc']
        image = request.FILES['file'].name
        post = Post(name=name, desc=desc, image=image)
        post.save()
        return redirect('post')  # Redirect to the same page to display all posts
    else:
        if not request.user.is_authenticated:
            messages.error(request, 'You need to Login First')

    # Retrieve all posts from the database
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'yourapp/post.html/', {'posts': posts})
