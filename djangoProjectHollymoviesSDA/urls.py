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
    countries, country, CreatorCreateView, CreatorUpdateView, CreatorDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),
    path('movies/', movies, name='movies'),
    path('movie/<int:pk>/', movie, name='movie'),
    path('genres/', genres, name='genres'),
    path('genre/<int:pk>/', genre, name='genre'),
    path('creators/', creators, name='creators'),
    path('creator/<int:pk>/', creator, name='creator'),
    # path('creatorform/', CreatorFormView.as_view(), name='creatorform'),
    path('creator/create/', CreatorCreateView.as_view(), name='creator_create'),
    path('creator/update/<int:pk>/', CreatorUpdateView.as_view(), name='creator_update'),
    path('creator/delete/<int:pk>/', CreatorDeleteView.as_view(), name='creator_delete'),
    path('countries/', countries, name='countries'),
    path('country/<int:pk>/', country, name='country'),
]
