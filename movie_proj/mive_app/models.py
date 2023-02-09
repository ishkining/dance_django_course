from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    director_email = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Actor(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Man'),
        (FEMALE, 'Woman'),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=MALE)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Movie(models.Model):
    EUR = 'E'
    DOL = 'D'
    RUB = 'R'
    CURRENCY_CHOICES = [
        (EUR, 'Euro'),
        (DOL, 'Dollars'),
        (RUB, 'Rubles'),
    ]
    name = models.CharField(max_length=40)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    year = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(default=100000)
    currency = models.CharField(max_length=1, choices=CURRENCY_CHOICES, default=RUB)
    slug = models.SlugField(default='', null=False, db_index=True)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True)
    actors = models.ManyToManyField(Actor)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)

    def get_url(self):
        return reverse('movie_detail', args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}'
