# software_house_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('like_post/<int:post_id>/', views.like_post, name='like_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('comment_post/<int:post_id>/', views.comment_post, name='comment_post'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('post/', views.post, name='post'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
