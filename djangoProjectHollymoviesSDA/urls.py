"""
URL configuration for djangoProjectHollymoviesSDA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.views import movies, home, movie, genres, genre, creators, creator, \
    countries, country, CreatorCreateView, CreatorUpdateView, \
    CreatorDeleteView, GenreCreateView, GenreUpdateView, GenreDeleteView, \
    CountryCreateView, CountryUpdateView, CountryDeleteView, MovieCreateView, \
    MovieUpdateView, MovieDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('movies/', movies, name='movies'),
    path('movie/<int:pk>/', movie, name='movie'),
    path('movie/create/', MovieCreateView.as_view(), name='movie_create'),
    path('movie/update/<int:pk>/', MovieUpdateView.as_view(), name='movie_update'),
    path('movie/delete/<int:pk>/', MovieDeleteView.as_view(), name='movie_delete'),
    path('genres/', genres, name='genres'),
    path('genre/<int:pk>/', genre, name='genre'),
    path('genre/create/', GenreCreateView.as_view(), name='genre_create'),
    path('genre/update/<int:pk>/', GenreUpdateView.as_view(), name='genre_update'),
    path('genre/delete/<int:pk>/', GenreDeleteView.as_view(), name='genre_delete'),
    path('creators/', creators, name='creators'),
    path('creator/<int:pk>/', creator, name='creator'),
    # path('creatorform/', CreatorFormView.as_view(), name='creatorform'),
    path('creator/create/', CreatorCreateView.as_view(), name='creator_create'),
    path('creator/update/<int:pk>/', CreatorUpdateView.as_view(), name='creator_update'),
    path('creator/delete/<int:pk>/', CreatorDeleteView.as_view(), name='creator_delete'),
    path('countries/', countries, name='countries'),
    path('country/<int:pk>/', country, name='country'),
    path('country/create/', CountryCreateView.as_view(), name='country_create'),
    path('country/update/<int:pk>/', CountryUpdateView.as_view(), name='country_update'),
    path('country/delete/<int:pk>/', CountryDeleteView.as_view(), name='country_delete'),
]
