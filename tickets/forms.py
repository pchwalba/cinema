from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import Movie, Ticket, Screening


class InstanceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form'

        if kwargs.get('instance'):
            button_title = "Save"
        else:
            button_title = "Create"
        self.helper.add_input(Submit("", button_title))


class MovieForm(InstanceForm):
    class Meta:
        model = Movie
        fields = ("title", "genre", "cast", "director", "runtime", "release_date", "storyline", "poster")
        widgets = {
            "release_date": forms.TextInput(attrs={'type': 'date'}),
        }


class ScreeningForm(InstanceForm):
    class Meta:
        model = Screening
        exclude = ("movie",)
        widgets = {
            "screening_time": forms.TextInput(attrs={'type': 'datetime-local'}),
        }


class TicketForm(InstanceForm):
    class Meta:
        model = Ticket
        exclude = ("screening",)


class SearchForm(forms.Form):
    search = forms.CharField(min_length=3, required=False)
    search_in = forms.ChoiceField(choices=(("title", "Title"), ("email", "E-Mail")), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "get"
        self.helper.add_input(Submit("", "Search"))
