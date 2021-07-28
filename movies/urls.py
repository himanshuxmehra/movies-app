from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('', views.movies, name='home'),
    path('movies', views.MoviesList, name='movies'),
    path('watch-<slug:slug>/', views.watch.as_view(), name='watch'),
    path('fetchNewMovies', views.fetchNewMovies, name='fetchnewmovies'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('subscribe', views.subscribe, name='subscribe'),
    path('tos', views.tos, name='tos'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
