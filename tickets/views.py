import datetime
from io import BytesIO

from PIL import Image
from django.contrib.messages.views import SuccessMessageMixin
from django.core.files.images import ImageFile
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView

from .forms import MovieForm, ScreeningForm, SearchForm
from .models import Movie, Screening, Ticket


class MovieList(ListView):
    """List of movies with current or future screenings"""
    model = Movie
    template_name = 'movie_list.html'
    now = timezone.now() - datetime.timedelta(hours=1)
    queryset = Movie.objects.all().filter(screening__screening_time__gte=now).distinct()


class MovieListAll(ListView):
    """List of all movie including past, or without screenings"""
    model = Movie
    template_name = 'movie_list.html'


class CreateMovie(SuccessMessageMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie_form.html'
    success_message = "Movie created successfully"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        poster = form.cleaned_data.get("poster")
        if poster:
            image = Image.open(poster)
            image.thumbnail((300, 300))
            image_data = BytesIO()
            image.save(fp=image_data,
                       format=poster.image.format)
            image_file = ImageFile(image_data)
            self.object.poster.save(poster.name, image_file)
        self.object.save()
        return super(CreateMovie, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'pk': self.object.pk})


class UpdateMovie(SuccessMessageMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movie_form.html'
    success_message = "Movie details updated"

    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'pk': self.object.pk})


class MovieDetail(DetailView):
    model = Movie
    template_name = 'movie_detail.html'

    def get_context_data(self, **kwargs):
        now = timezone.now() - datetime.timedelta(hours=1)
        # allows to buy tickets for movies which already started
        context = super().get_context_data(**kwargs)
        context["screenings"] = Screening.objects.filter(movie=self.object.pk, screening_time__gte=now)

        return context


class CreateScreening(SuccessMessageMixin, CreateView):
    model = Screening
    form_class = ScreeningForm
    template_name = "movie_form.html"
    success_message = "Screening created successfully"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.movie = Movie.objects.get(pk=self.kwargs.get('movie_pk'))
        self.object.save()

        return super(CreateScreening, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('movie_detail', kwargs={'pk': self.object.movie_id})


class ScreeningDetail(DetailView):
    model = Screening
    template_name = 'screening_detail.html'


class TicketLatest(DetailView):
    model = Ticket
    template_name = 'ticket.html'


class SearchView(View):
    template_name = "search.html"
    form_class = SearchForm

    def get(self, request):
        form = self.form_class
        search = self.request.GET.get('search')
        search_in = self.request.GET.get('search_in')
        context = {'form': form, 'search_in': search_in}
        if search_in == 'title':
            context['object_list'] = Movie.objects.filter(title__icontains=search)
        elif search_in == 'email':
            context['object_list'] = Ticket.objects.filter(email__icontains=search)

        return render(self.request, self.template_name, context)
