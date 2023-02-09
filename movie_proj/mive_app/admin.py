from django.contrib import admin
from .models import Movie, Director, Actor
from django.db.models import QuerySet


# Register your models here.

class RatingFilter(admin.SimpleListFilter):
    title = 'Rating Filter'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Low'),
            ('from 40 to 59', 'Medium'),
            ('from 60 to 79', 'High'),
            ('>=80', 'Highest'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        elif self.value() == 'from 40 to 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)
        elif self.value() == 'from 60 to 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)
        else:
            return queryset.filter(rating__gte=80)
        return queryset


class MovieAdmin(admin.ModelAdmin):
    #fields = ['name', 'rating']
    #exclude = ['slug', 'budget']
    readonly_fields = ['year']
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'rating', 'currency', 'budget']
    list_editable = ['rating', 'currency', 'budget']
    ordering = ['rating']
    list_per_page = 3
    actions = ['set_dollars']
    search_fields = ['name__startswith']
    list_filter = ['name', 'currency', RatingFilter]
    filter_horizontal = ['actors']

    @admin.display(ordering='rating', description='Status')
    def rating_status(self, movie: Movie):
        if movie.rating < 50:
            return 'Why I should watch'
        elif movie.rating < 70:
            return 'Maybe i will watch'
        else:
            return 'Good'

    @admin.action(description='Set currency to USD')
    def set_dollars(self, request, queryset: QuerySet):
        queryset.update(currency=Movie.DOL)


admin.site.register(Movie, MovieAdmin)
admin.site.register(Director)
admin.site.register(Actor)
