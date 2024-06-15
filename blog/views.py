from django.shortcuts import render
from django.views import generic
from .models import Post

# create views here

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "post_list.html"