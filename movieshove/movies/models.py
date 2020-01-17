from django.db import models

# Create your models here.


class Movie(models.Model):
    NOT_RATED = 0
    RATED_G = 1
    RATED_PG = 2
    RATED_R = 3
    RATINGS = (
        (NOT_RATED, 'NR - Not Rated'),
        (RATED_G, 'G - General Audience'),
        (RATED_PG, 'PG - Parental Guidance'),
        (RATED_R, 'R - Restricted'),
    )
    title = models.CharField(max_length=180)
    plot = models.TextField(max_length=1000)
    year = models.PositiveIntegerField()
    slug = models.SlugField(max_length=200, unique=True)
    rating = models.IntegerField(choices=RATINGS, default=NOT_RATED)
    runtime = models.PositiveIntegerField()
    trailer = models.URLField(blank=True)
    poster = models.ImageField(upload_to='images/', default='images/default.jpg')
    date_added = models.DateTimeField(auto_now=True)
    hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        self.hit += 1
        self.save()
        return '{} ({})'.format(self.title, self.year)

    class Meta:
        get_latest_by = 'date_added'
