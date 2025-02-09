from datetime import datetime

from django.db import models
from django.db.models import Model, CharField, ManyToManyField, IntegerField, \
    TextField, DateField, DateTimeField, ForeignKey


class Genre(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"Genre(name={self.name}"


class Country(Model):
    name = CharField(max_length=32, null=False, blank=False, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Countries"

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"Country(name={self.name})"


class Movie(Model):
    title_orig = CharField(max_length=64, null=False, blank=False)
    title_cz = CharField(max_length=64, null=True, blank=True)
    genres = ManyToManyField(Genre, blank=True, related_name='movies')
    countries = ManyToManyField(Country, blank=True, related_name='movies')
    length = IntegerField(null=True, blank=True)
    description = TextField(null=True, blank=True)
    released_date = DateField(null=True, blank=True)
    released_year = IntegerField(null=True, blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)
    actors = ManyToManyField("Creator", blank=True, related_name='acting')
    directors = ManyToManyField("Creator", blank=True, related_name='directing')

    class Meta:
        ordering = ['title_orig']
        verbose_name_plural = "Movies"

    def __str__(self):
        return f"{self.title_orig} ({self.released_year})"

    def __repr__(self):
        return f"Movie(title_orig={self.title_orig})"

    def released_date_cz(self):
        if self.released_date:
            return datetime.strftime(self.released_date, "%d. %m. %Y")
        return None


class Creator(Model):
    name = CharField(max_length=32, null=True, blank=True)
    surname = CharField(max_length=32, null=True, blank=True)
    alias = CharField(max_length=32, null=True, blank=True)
    date_of_birth = DateField(null=True, blank=True)
    date_of_death = DateField(null=True, blank=True)
    country = ForeignKey(Country, null=True, blank=True, related_name='creators', on_delete=models.SET_NULL)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __repr__(self):
        return f"Creator {self.name} {self.surname})"

    def age(self):
        if self.date_of_death:
            return (self.date_of_death - self.date_of_birth).days
        return datetime.date.today() - self.date_of_birth

    class Meta:
        ordering = ['surname']
