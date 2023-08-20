from django.test import TestCase
from tickets.models import Movie, Screening, Ticket

import datetime


class TestMovie(TestCase):
    def setUp(self):
        self.date = datetime.date(2020, 1, 5)
        self.movie = Movie.objects.create(
            title='dark tower', genre="HORROR",
            cast="Elba", director="Andrzej Wajda",
            runtime=120, release_date=self.date,
            storyline="Roland idzie do wieży")
        self.screening = Screening.objects.create(
            movie=self.movie,
            screening_time=self.date,
            price=10)
        self.ticket = Ticket.objects.create(
            name="Michał",
            screening=self.screening,
            seat=15, )

    def test_create_movie(self):
        self.assertIsInstance(self.movie, Movie)

    def test_create_ticket(self):
        self.assertIsInstance(self.ticket, Ticket)
