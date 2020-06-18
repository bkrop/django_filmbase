from main.models import Person
from django.shortcuts import render
from django.views.generic import CreateView, DetailView

class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'
    template_name = 'main/create_person.html'

class PersonDetailView(DetailView):
    model = Person
    template_name = 'main/detail_person.html'

