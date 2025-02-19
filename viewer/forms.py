import re
from datetime import date

from django.core.exceptions import ValidationError
from django.forms import Form, CharField, DateField, ModelChoiceField, \
    Textarea, ModelForm, NumberInput

from viewer.models import Country, Creator, Genre, Movie

"""
class CreatorForm(Form):
    name = CharField(max_length=32, required=False)
    surname = CharField(max_length=32, required=False)
    alias = CharField(max_length=32, required=False)
    date_of_birth = DateField(required=False)
    date_of_death = DateField(required=False)
    country = ModelChoiceField(queryset=Country.objects, required=False)
    biography = CharField(widget=Textarea, required=False)
"""


class CreatorModelForm(ModelForm):
    class Meta:
        model = Creator
        fields = '__all__'
        # fields = ['name', 'surname', 'alias', 'date_of_birth', 'date_of_death']
        # exclude = ['biography']

        labels = {
            'name': 'Jméno',
            'surname': 'Příjmení',
            'alias': 'Umělecké jméno',
            'date_of_birth': 'Narození',
            'date_of_death': 'Úmrtí',
            'country': 'Země',
            'biography': 'Biografie',
        }
        help_texts = {
            'biography': 'Zde zadejte biografii tvůrce.'
        }
        error_messages = {
            # TODO: později dodělat
        }

    date_of_birth = DateField(required=False,
                              widget=NumberInput(attrs={'type': 'date'}),
                              label="Narození")
    date_of_death = DateField(required=False,
                              widget=NumberInput(attrs={'type': 'date'}),
                              label="Úmrtí")

    def clean_name(self):
        initial = self.cleaned_data['name']
        result = initial
        if initial:
            result = initial.capitalize()
        return result

    def clean_surname(self):
        initial = self.cleaned_data['surname']
        result = initial
        if initial:
            result = initial.capitalize()
        return result

    def clean_alias(self):
        initial = self.cleaned_data['alias']
        result = initial
        if initial:
            result = initial.capitalize()
        return result

    def clean_date_of_birth(self):
        initial = self.cleaned_data['date_of_birth']
        if initial and initial > date.today():
            raise ValidationError("Datum narození nesmí být v budoucnosti")
        return initial

    def clean_date_of_death(self):
        initial = self.cleaned_data['date_of_death']
        if initial and initial > date.today():
            raise ValidationError("Datum úmrtí nesmí být v budoucnosti")
        return initial

    def clean_biography(self):
        initial = self.cleaned_data['biography']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        cleaned_data = super().clean()
        initial_name = cleaned_data['name']
        initial_surname = cleaned_data['surname']
        initial_alias = cleaned_data['alias']
        if not initial_surname and not initial_alias:
            raise ValidationError("Je nutné zadat příjmení nebo "
                                  "umělecké jméno (nebo oboje).")

        initial_date_of_birth = cleaned_data.get('date_of_birth')
        initial_date_of_death = cleaned_data.get('date_of_death')
        if (initial_date_of_birth
                and initial_date_of_death
                and initial_date_of_death <= initial_date_of_birth):
           raise ValidationError("Datum úmrtí nesmí "
                                 "být dříve než datum narození.")

        return cleaned_data


class GenreModelForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

        labels = {
            'name': 'Název'
        }

    def clean_name(self):
        initial = self.cleaned_data['name']
        return initial.capitalize()


class CountryModelForm(ModelForm):
    class Meta:
        model = Country
        fields = '__all__'

        labels = {
            'name': 'Název'
        }

    def clean_name(self):
        initial = self.cleaned_data['name']
        return initial.capitalize()


class MovieModelForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        labels = {
            'title_orig': 'Původní název',
            'title_cz': 'Český název',
            'genres': 'Žánry',
            'countries': 'Země',
            'directors': 'Režie',
            'actors': 'Hráli',
            'length': 'Délka',
            'description': 'Popis',
            'released_date': 'Datum premiéry',
            'released_year': 'Rok premiéry',
        }
        help_texts = {
            'length': 'Délka filmu v minutách',
            'description': 'Popis, stručný obsah nebo jiné k filmu',
        }
        error_messages = {
            'title_orig': {
                'required': 'Tento údaj je povinný',
            }
        }

    released_date = DateField(required=False,
                              widget=NumberInput(attrs={'type': 'date'}),
                              label="Datum premiéry")

    def clean_title_orig(self):
        initial = self.cleaned_data['title_orig']
        return initial.capitalize()

    def clean_title_cz(self):
        initial = self.cleaned_data['title_cz']
        if initial:
            return initial.capitalize()
        return initial

    def clean_length(self):
        initial = self.cleaned_data['length']
        if initial and initial <= 0:
            raise ValidationError("Udávaná délka filmu musí být kladné číslo")

    def clean_description(self):
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        cleaned_data = super().clean()
        released_date = cleaned_data.get('released_date')
        if released_date:
            cleaned_data['released_year'] = released_date.year
        return cleaned_data
