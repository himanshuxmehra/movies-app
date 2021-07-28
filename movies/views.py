import requests

from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from movieshove import settings
from .models import Movie

TMDB_API_KEY = settings.TMDB_API_KEY

def movies(request):
    model = Movie.objects.all()
    pop = Movie.objects.all().order_by('-date_added')
    latest_post = Movie.objects.latest()
    context = {'allmovies': model, 'pop': pop, 'last': latest_post}
    return render(request, 'home.html', context)

def fetchNewMovies(request):
    url = 'https://api.themoviedb.org/3/trending/movie/day?api_key='+ TMDB_API_KEY
    r = requests.get(url)
    r = r.json()
    count = 0
    newMoviesAdded = []
    for i in r['results']:
        url ='https://api.themoviedb.org/3/movie/'+str(i['id'])+'?api_key=8a88b92a125f64ec5559f02b4a6195c8&append_to_response=videos'
        extra = requests.get(url)
        extra = extra.json()
        trailer=""
        if(len(extra['videos']['results']) !=0):
            trailer = 'https://www.youtube.com/embed/' + extra["videos"]["results"][0]["key"]
        if not Movie.objects.filter(slug=i['id']).exists() :
            if(i['adult']):
                rated = 3
            else:
                rated = 2
            count+=1
            newMoviesAdded.append(i['title'])
            newMovie = Movie.objects.create(title = i['title'] ,plot = i['overview'] ,year = int(i['release_date'][0:4]),slug= i['id'],rating = rated,runtime = extra['runtime'], trailer = trailer,cover="https://image.tmdb.org/t/p/original/"+i['backdrop_path'],poster="https://image.tmdb.org/t/p/original/"+i['poster_path'], hit = 0)
    context = { "count" : count, 'newMovies': newMoviesAdded}
    return render(request, 'fetchNewMovies.html',context)
   

def MoviesList(request):
    model = Movie.objects.all()
    latest_post = Movie.objects.latest()
    context = {'allmovies': model, 'last': latest_post}
    return render(request, 'movies.html', context)


   
class SearchView(ListView):
    model = Movie
    template_name = 'search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       print(query)
       if query:
            url = 'https://api.themoviedb.org/3/search/movie?api_key='+ TMDB_API_KEY +'&query='+query
            r = requests.get(url)
            r = r.json()
            print(r)

            newMoviesAdded = []
            for i in r['results']:
                url ='https://api.themoviedb.org/3/movie/'+str(i['id'])+'?api_key='+ TMDB_API_KEY +'&append_to_response=videos'
                extra = requests.get(url)
                extra = extra.json()
                trailer=""
                if(len(extra['videos']['results']) !=0):
                    trailer = 'https://www.youtube.com/embed/' + extra["videos"]["results"][0]["key"]
                if not Movie.objects.filter(slug=i['id']).exists() :
                    if(i['adult']):
                        rated = 3
                    else:
                        rated = 2
                    newMovie = Movie.objects.create(title = i['title'] ,plot = i['overview'] ,year = int(i['release_date'][0:4]),slug= i['id'],rating = rated,runtime = extra['runtime'], trailer = trailer,cover="https://image.tmdb.org/t/p/original/"+str(i['backdrop_path']),poster="https://image.tmdb.org/t/p/original/"+str(i['poster_path']), hit = 0)
            postresult = Movie.objects.filter(title__contains=query)
            result = postresult
            print(postresult)
       else:
           result = None
       return result

class watch(DetailView):
    model = Movie
    template_name = 'watch.html'
