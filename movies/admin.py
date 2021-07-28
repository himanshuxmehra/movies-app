from django.contrib import admin

# Register your models here.
from .models import Movie, Subscribers


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'date_added', 'hit')
    list_filter = ("date_added",)
    search_fields = ['title', 'year']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Movie, MovieAdmin)

admin.site.register(Subscribers)
