from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('', views.movies, name='home'),
    path('movies', views.MoviesList, name='movies'),
    path('watch-<slug:slug>/', views.watch.as_view(), name='watch'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
