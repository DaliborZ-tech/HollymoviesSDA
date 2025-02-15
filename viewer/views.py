from django.shortcuts import render, redirect
from viewer.models import *


def movies(request):
    movies_ = Movie.objects.all()
    context = {'movies': movies_}
    return render(request=request,
                  template_name='movies.html',
                  context=context)


def movie(request, pk):
    if Movie.objects.filter(id=pk).exists():
        movie_ = Movie.objects.get(id=pk)
        context = {'movie': movie_}
        return render(request=request,
                      template_name='movie.html',
                      context=context)
    else:
        return redirect("home")


def home(request):
    return render(request=request,
                  template_name='home.html')


def genres(request):
    genres_ = Genre.objects.all()
    context = {'genres': genres_}
    return render(request=request, template_name='genres.html', context=context)


def genre(request, pk):
    if Genre.objects.filter(id=pk).exists():
        return render(request=request, template_name='genre.html',
                      context={'genre': Genre.objects.get(id=pk)})
    return redirect("genres")


def creators(request):
    creators_ = Creator.objects.all()
    context = {'creators': creators_}
    return render(request=request, template_name='creators.html',
                  context=context)


def creator(request, pk):
    if Creator.objects.filter(id=pk).exists():
        return render(request=request, template_name='creator.html',
                      context={'creator': Creator.objects.get(id=pk)})
    return redirect("creators")


def countries(request):
    countries_ = Country.objects.all()
    context = {'countries': countries_}
    return render(request=request, template_name='countries.html', context=context)


def country(request, pk):
    if Country.objects.filter(id=pk).exists():
        return render(request=request, template_name='country.html',
                      context={'country': Country.objects.get(id=pk)})
    return redirect("Countries")
