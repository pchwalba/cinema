from django.db import models


# Create your models here.


class Movie(models.Model):
    """Movie"""

    class MovieGenres(models.TextChoices):
        ACTION = "action", "Action"
        ADVENTURE = "adventure", "Adventure"
        ANIMATION = "animation", "Animation"
        COMEDY = "comedy", "Comedy"
        CRIME = "crime", "Crime"
        DRAMA = "drama", 'Drama'
        FANTASY = "fantasy", "Fantasy"
        HORROR = "horror", "Horror"
        MYSTERY = "mystery", "Mystery"
        ROMANCE = "romance", "Romance"
        SCI_FI = "sci_fi", "Sci-Fi"
        THRILLER = "thriller", "Thriller"

    title = models.CharField(max_length=50, help_text="Title of the movie")
    genre = models.CharField(verbose_name="Genre of the Movie", choices=MovieGenres.choices, max_length=20)
    cast = models.CharField(max_length=50, help_text="Cast of the movie")
    director = models.CharField(max_length=50, help_text="Director of The movie")
    runtime = models.PositiveIntegerField(help_text="Runtime of the movie in minutes")
    release_date = models.DateField(verbose_name="Date of the initial release")
    storyline = models.TextField(help_text="Storyline of the movie")
    poster = models.ImageField(upload_to="movie_posters/", null=True, blank=True)

    def __str__(self):
        return self.title


class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screening_time = models.DateTimeField(help_text="date and time of the screening")
    price = models.FloatField(help_text="Price of the tickets")

    def __str__(self):
        return "{} {}".format(self.movie, str(self.screening_time))


class Ticket(models.Model):
    name = models.CharField(max_length=20, help_text="Name on the Ticket")
    phone_number = models.CharField(max_length=9, null=True, help_text="Phone numer of the person making reservation")
    email = models.EmailField(null=True, help_text="Email address")
    screening = models.ForeignKey(Screening, on_delete=models.RESTRICT)
    seat = models.PositiveIntegerField()
    discount = models.BooleanField(default=False)

    def __str__(self):
        return "{} {}".format(self.screening, self.name)
