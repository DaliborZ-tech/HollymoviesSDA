from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, UpdateView, DeleteView

from djangoProjectHollymoviesSDA.settings import DEBUG
from viewer.forms import CreatorModelForm, GenreModelForm, CountryModelForm, \
    MovieModelForm
from viewer.models import *


def movies(request):
    movies_ = Movie.objects.all()
    countries_list = Country.objects.filter(movies__isnull=False).distinct()
    context = {'movies': movies_, 'countries': countries_list}
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


class MovieCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = MovieModelForm
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.add_movie'

    def form_invalid(self, form):
        if DEBUG:
            print(form.errors)
        return super().form_invalid(form)


class MovieUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = MovieModelForm
    model = Movie
    permission_required = 'viewer.change_movie'

    def get_success_url(self):
        return reverse_lazy('movie', kwargs={'pk': self.object.id})


class MovieDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.delete_movie'


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


class GenreCreateView(PermissionRequiredMixin, CreateView):
    template_name = "form.html"
    form_class = GenreModelForm
    success_url = reverse_lazy("genres")
    permission_required = 'viewer.add_genre'

    def form_invalid(self, form):
        if DEBUG:
            print("Genre model form invalid")
        return super().form_invalid(form)


class GenreUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = GenreModelForm
    model = Genre
    permission_required = 'viewer.change_genre'

    def get_success_url(self):
        return reverse_lazy('genre', kwargs={'pk': self.object.pk})

    def form_invalid(self, form):
        print("Form 'GenreModelForm' not valid")
        return super().form_invalid(form)


class GenreDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Genre
    success_url = reverse_lazy('genres')
    permission_required = 'viewer.delete_genre'


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


"""
class CreatorFormView(FormView):
    template_name = 'form.html'
    form_class = CreatorModelForm
    success_url = reverse_lazy('creators')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Creator.objects.create(
            name=cleaned_data['name'],
            surname=cleaned_data['surname'],
            alias=cleaned_data['alias'],
            date_of_birth=cleaned_data['date_of_birth'],
            date_of_death=cleaned_data['date_of_death'],
            country=cleaned_data['country'],
            biography=cleaned_data['biography'],
        )
        return result

    def form_invalid(self, form):
        print("Form 'CreatorModelForm' not valid")
        return super().form_invalid(form)
"""


class CreatorCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = CreatorModelForm
    success_url = reverse_lazy('creators')
    permission_required = 'viewer.add_creator'

    def form_invalid(self, form):
        print("Form 'CreatorModelForm' not valid")
        return super().form_invalid(form)


class CreatorUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = CreatorModelForm
    model = Creator
    permission_required = 'viewer.change_creator'

    def get_success_url(self):
        return reverse_lazy('creator', kwargs={'pk': self.object.pk})

    def form_invalid(self, form):
        print("Form 'CreatorModelForm' not valid")
        return super().form_invalid(form)


class CreatorDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Creator
    success_url = reverse_lazy('creators')
    permission_required = 'viewer.delete_creator'


def countries(request):
    countries_ = Country.objects.all()
    context = {'countries': countries_}
    return render(request=request, template_name='countries.html', context=context)


def country(request, pk):
    if Country.objects.filter(id=pk).exists():
        return render(request=request, template_name='country.html',
                      context={'country': Country.objects.get(id=pk)})
    return redirect("Countries")


class CountryCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = CountryModelForm
    success_url = reverse_lazy('countries')
    permission_required = 'viewer.add_country'

    def form_invalid(self, form):
        print("Form 'CountryModelForm' not valid")
        return super().form_invalid(form)


class CountryUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'form.html'
    form_class = CountryModelForm
    model = Country
    permission_required = 'viewer.change_country'

    def get_success_url(self):
        return reverse_lazy('country', kwargs={'pk': self.object.pk})

    def form_invalid(self, form):
        print("Form 'CountryModelForm' not valid")
        return super().form_invalid(form)


class CountryDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'confirm_delete.html'
    model = Country
    success_url = reverse_lazy('countries')
    permission_required = 'viewer.delete_country'
