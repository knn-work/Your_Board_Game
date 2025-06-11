from django.shortcuts import render

from blog.models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()  # select * from post
    context = {"title": "Главная страница", "posts": posts}
    return render(request=request, context=context, template_name="blog/index.html")
