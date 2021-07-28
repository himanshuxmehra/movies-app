from django.apps import AppConfig


class MoviesConfig(AppConfig):
    name = 'movies'
    def ready(self):
        from movies import newsletter
        newsletter.start()