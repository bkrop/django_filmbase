from main.models import Person, Rate, Movie
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView
from .forms import RateForm
from django.views.generic.edit import FormMixin
from django.urls import reverse
from blog.models import Post
from itertools import chain
from django.shortcuts import render
from django.db.models import Q
from django.db.models import Avg
from .forms import PersonForm

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'main/create_person.html'

class PersonDetailView(FormMixin, DetailView):
    model = Person
    template_name = 'main/detail_person.html'
    context_object_name = 'person'
    form_class = RateForm

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        context['form'] = RateForm(initial={'person': self.object})
        context['my_rate'] = Rate.objects.filter(
                sender=self.request.user,
                person=self.get_object()).first()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        Rate.objects.update_or_create(
            sender=self.request.user, 
            person=self.object,
            defaults={'choice': form.cleaned_data['choice']}
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('detail_person', kwargs={'slug': self.object.slug})

class MovieCreateView(CreateView):
    model = Movie
    fields = '__all__'
    template_name = 'main/create_movie.html'

class MovieListView(ListView):
    model = Movie
    template_name = 'main/list_movie.html'
    context_object_name = 'movies'

    def get_queryset(self):
        qs = Movie.objects.annotate(average_stars = Avg('rate__choice')).order_by('-average_stars')
        return qs

class MovieDetailView(FormMixin, DetailView):
    model = Movie
    template_name = 'main/detail_movie.html'
    context_object_name = 'movie'
    form_class = RateForm

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['form'] = RateForm(initial={'movie': self.object})
        context['my_rate'] = Rate.objects.filter(
                sender=self.request.user,
                movie=self.get_object()).first()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        Rate.objects.update_or_create(
            sender=self.request.user, 
            movie=self.object,
            defaults={'choice': form.cleaned_data['choice']}
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('detail_movie', kwargs={'slug': self.object.slug})

def search(request):
    query = request.GET.get('search')
    people = Person.objects.filter(Q(full_name__contains=query))
    movies = Movie.objects.filter(Q(title__contains=query))
    posts = Post.objects.filter(Q(title__contains=query))
    results = chain(people, movies, posts)
    context = {
        'results': results
    }
    return render(request, 'main/results.html', context=context)