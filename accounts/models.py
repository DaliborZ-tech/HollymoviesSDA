from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model, OneToOneField, CASCADE, DateField, \
    TextField


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    date_of_birth = DateField(blank=True, null=True)
    biography = TextField(blank=True)

    class Meta:
        ordering = ['user__username']

    def __repr__(self):
        return f'Profile for user {self.user}'

    def __str__(self):
        return f'{self.user.username}'
