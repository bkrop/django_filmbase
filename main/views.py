from main.models import Person
from django.shortcuts import render
from django.views.generic import CreateView

class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'
    template_name = 'main/create_person.html'

# Create your views here.
