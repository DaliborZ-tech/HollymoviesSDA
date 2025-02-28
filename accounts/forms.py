from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.transaction import atomic
from django.forms import PasswordInput, NumberInput, Textarea
from django.forms.fields import CharField, DateField

from accounts.models import Profile


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'password1', 'password2']
        labels = {
            'username': 'Uživatelské jméno',
            'first_name': 'Jméno',
            'last_name': 'Příjmení',
            'email': 'E-mail',
        }
    date_of_birth = DateField(
        widget=NumberInput(attrs={'type': 'date'}),
        label="Datum narození",
        required=False
    )
    biography = CharField(
        widget=Textarea,
        label='Biografie',
        required=False
    )
    password1 = CharField(
        widget=PasswordInput(attrs={'placeholder': 'Heslo'}),
        label='Heslo'
    )
    password2 = CharField(
        widget=PasswordInput(attrs={'placeholder': 'Heslo znova'}),
        label='Heslo znova'
    )

    @atomic
    def save(self, commit=True):
        self.instance.is_active = True
        user = super().save(commit)

        date_of_birth = self.cleaned_data.get('date_of_birth')
        biography = self.cleaned_data.get('biography')
        profile = Profile(user=user, date_of_birth=date_of_birth, biography=biography)
        profile.save()
        if commit:
            profile.save()
        return user

