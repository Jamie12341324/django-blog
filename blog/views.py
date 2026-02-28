from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.all()
    #queryset = Post.objects.all().order_by("-created_on")
    #queryset = Post.objects.filter(author=2)
    #queryset = Post.objects.filter(status=1)
    #template_name = "post_list.html"
    template_name = "blog/index.html"
    paginate_by = 6