from django.shortcuts import render
from .models import People, Post

# Create your views here.


def people(request):
    people_list = People.objects.all()

    return render(request, 'person/people.html', {'people_list': people_list})


def post(request, pk):
    post_pk = pk
    author = People.objects.get(pk=post_pk)
    post_list = Post.objects.all().filter(name=post_pk)

    return render(request, 'person/post.html', {'post_list': post_list, 'post_pk': post_pk, 'author': author})
