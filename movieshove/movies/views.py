from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Movie

# Create your views here.


def movies(request):
    model = Movie.objects.all()
    pop = Movie.objects.all().order_by('-date_added')
    latest_post = Movie.objects.latest()
    context = {'allmovies': model, 'pop': pop, 'last': latest_post}
    return render(request, 'home.html', context)


def MoviesList(request):
    model = Movie.objects.all()
    latest_post = Movie.objects.latest()
    context = {'allmovies': model, 'last': latest_post}
    return render(request, 'movies.html', context)


class watch(DetailView):
    model = Movie
    template_name = 'watch.html'
