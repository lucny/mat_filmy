from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


def attachment_path(instance, filename):
    return 'film/' + str(instance.film.id) + '/attachments/' + filename


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Genre name',
    help_text='Enter a film genre (e.g. sci-fi, comedy)')

    class Meta:
        verbose_name = 'Žánr'
        verbose_name_plural = 'Žánry'
        ordering = ['name']

    def __str__(self):
        return self.name


class Film(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    plot = models.TextField(blank=True, null=True, verbose_name='Plot')
    release_date = models.DateField(blank=True, null=True,
                                    help_text='Please use the following format: <em>YYYYMM-DD</em>.',
                                    verbose_name='Release date')
    runtime = models.IntegerField(blank=True, null=True,
                                  help_text='Please enter an integer value (minutes)',
                                  verbose_name='Runtime')
    poster = models.ImageField(upload_to='film/posters/%Y/%m/%d/', blank=True, null=True,
                               verbose_name="Poster")
    rate = models.FloatField(default=5.0,
                             validators=[MinValueValidator(1.0), MaxValueValidator(10.0)],
                             null=True, help_text='Please enter an float value (range 1.0 - 10.0)',
                             verbose_name='Rate')
    genres = models.ManyToManyField(Genre, help_text='Select a genre for this film')

    class Meta:
        verbose_name = 'Film'
        verbose_name_plural = 'Filmy'
        ordering = ['-release_date', 'title']

    def __str__(self):
        return f'{self.title}, year: {str(self.release_date.year)}, rate:{str(self.rate)}'

    def get_absolute_url(self):
        return reverse('film-detail', args=[str(self.id)])


class Attachment(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    last_update = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=attachment_path, null=True, verbose_name='File')
    TYPE_OF_ATTACHMENT = (
        ('audio', 'Audio'),
        ('image', 'Image'),
        ('text', 'Text'),
        ('video', 'Video'),
        ('other', 'Other'),
    )
    type = models.CharField(max_length=10, choices=TYPE_OF_ATTACHMENT, blank=True,
        default='image', help_text='Select allowed attachment type',
        verbose_name='Attachment type')
    film = models.ForeignKey(Film, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Příloha'
        verbose_name_plural = 'Přílohy'
        ordering = ['-last_update', 'type']

    def __str__(self):
        return f'{self.title}, ({self.type})'


class Artist(models.Model):
    first_name = models.CharField(verbose_name='Jméno', help_text='Zadejte křestní jméno umělce', max_length=50)
    second_name = models.CharField(verbose_name='Příjmení', help_text='Zadejte příjmení umělce', max_length=50)
    birth = models.DateField(verbose_name='Datum narození', help_text='Zadejte datum narození umělce')
    photo = models.ImageField(upload_to='artists', blank=True, null=True, verbose_name='Fotka', help_text='Vložte fotku umělce')
    bio = models.TextField(blank=True, null=True, verbose_name='Životopis', help_text='Napište informace o životě umělce')
    GENDER = [
        ('muž', 'Muž'),
        ('žena', 'Žena'),
        ('jiné', 'Jiné'),
    ]
    gender = models.CharField(choices=GENDER, verbose_name='Pohlaví', help_text='Zadejte pohlaví umělce', max_length=10, default='žena')
    film = models.ManyToManyField('Film', verbose_name='Název filmu', help_text='Vyberte filmy spojené s umělcem')

    class Meta:
        verbose_name = 'Umělec'
        verbose_name_plural = 'Umělci'
        ordering = ['-birth', 'second_name']

    def __str__(self):
        return f'{self.second_name}, {self.first_name} (nar. {self.birth.strftime("%d. %m.")})'