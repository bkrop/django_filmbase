from django.db import models

class Person(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    date_of_birth = models.DateField(null=False, blank=False)

class Movie(models.Model):
    title = models.CharField(null=False, blank=False, max_length=100)
    description = models.CharField(null=False, blank=False, max_length=400)
    date_of_realease = models.DateField(null=False, blank=False)
    rating = models.FloatField(blank=False, null=False)
    kind = models.CharField(null=False, blank=False, max_length=100)
    actors = models.ManyToManyField(Person, related_name='Starred_in')
    directors = models.ManyToManyField(Person, related_name='Directed')
    scenarists = models.ManyToManyField(Person, related_name='Wrote_the_script')

