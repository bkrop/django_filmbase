from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
from django.contrib.auth.models import User
from django.urls import reverse

RATE_CHOICES = [(i, i) for i in range(1, 11)]

class Person(models.Model):
    full_name = models.CharField(null=False, blank=False, max_length=100)
    date_of_birth = models.DateField(null=False, blank=False)
    slug = models.SlugField(null=True, blank=True)
    avatar = models.ImageField(default='default.jpg', null=True, blank=True)
    is_accepted = models.BooleanField(default=False)
    
    def get_average(self):
        rates = self.rate_set.all().values_list('choice', flat=True)
        if rates:
            average = (sum(rates))/len(rates)
            return average
        return "Brak oceny"

    def __str__(self):
        return f"{self.full_name}"

    def get_absolute_url(self):
        return reverse('detail_person', kwargs={'slug': self.slug })

    def get_class(self):
        return self.__class__.__name__

class Movie(models.Model):
    title = models.CharField(null=False, blank=False, max_length=100, verbose_name='Tytuł')
    description = models.CharField(null=False, blank=False, max_length=400, verbose_name='Opis')
    date_of_realease = models.DateField(null=False, blank=False, verbose_name='Data premiery')    
    kind = models.CharField(null=False, blank=False, max_length=100, verbose_name='Gatunek')
    actors = models.ManyToManyField(Person, related_name='Starred_in')
    directors = models.ManyToManyField(Person, related_name='Directed')
    scenarists = models.ManyToManyField(Person, related_name='Wrote_the_script')
    slug = models.SlugField(null=True, blank=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    def get_average(self):
        rates = self.rate_set.all().values_list('choice', flat=True)
        if rates:
            average = (sum(rates))/len(rates)
            return average
        return "Brak oceny"

    def get_absolute_url(self):
        return reverse('detail_movie', kwargs={'slug': self.slug })

    def get_class(self):
        return self.__class__.__name__

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Person)
pre_save.connect(slug_generator, sender=Movie)

class Rate(models.Model):
    class Meta:
        unique_together = (('sender', 'person'), ('sender', 'movie'),)

    choice = models.IntegerField(null=False, blank=False, choices=RATE_CHOICES,
                                verbose_name='Twoja ocena')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True)