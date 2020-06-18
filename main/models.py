from django.db import models

class Person(models.Model):
    full_name = models.CharField(null=False, blank=False, max_length=100)
    date_of_birth = models.DateField(null=False, blank=False)
    #avatar = models.ImageField()

class Movie(models.Model):
    title = models.CharField(null=False, blank=False, max_length=100, verbose_name='Tytuł')
    description = models.CharField(null=False, blank=False, max_length=400, verbose_name='Opis')
    date_of_realease = models.DateField(null=False, blank=False, verbose_name='Data premiery')
    rating = models.FloatField(blank=False, null=False, verbose_name='Ocena')
    kind = models.CharField(null=False, blank=False, max_length=100, verbose_name='Gatunek')
    actors = models.ManyToManyField(Person, related_name='Starred_in')
    directors = models.ManyToManyField(Person, related_name='Directed')
    scenarists = models.ManyToManyField(Person, related_name='Wrote_the_script')

