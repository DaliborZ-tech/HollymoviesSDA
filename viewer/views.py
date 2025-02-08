from django.shortcuts import render, redirect
from viewer.models import *


def movies(request):
    movies_ = Movie.objects.all()
    context = {'movies': movies_}
    return render(request=request,
                  template_name='movies.html',
                  context=context)


def home(request):
    return render(request=request,
                  template_name='home.html')


def movie(request, pk):
    if Movie.objects.filter(id=pk).exists():
        movie_ = Movie.objects.get(id=pk)
        context = {'movie': movie_}
        return render(request=request,
                      template_name='movie.html',
                      context=context)
    else:
        return redirect("home")

