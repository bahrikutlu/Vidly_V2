from django.contrib import admin
from . models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):  # representation of a model in admin interface
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):  # representation of a model in admin interface
    exclude = ('date_created', )
    list_display = ('title', 'number_in_stock', 'daily_rate')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)