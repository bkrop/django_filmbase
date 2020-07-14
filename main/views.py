from main.models import Person, Rate, Movie
from django.http import HttpResponseRedirect, JsonResponse
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.urls import reverse
from blog.models import Post
from itertools import chain
from django.shortcuts import render
from django.db.models import Q
from django.db.models import Avg
from .forms import PersonForm, MovieForm, RateForm
from django.forms.models import model_to_dict

class PersonCreateView(LoginRequiredMixin, CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'main/create_person.html'

    def get_context_data(self, **kwargs):
        context = super(PersonCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Stwórz osobę'
        return context

class PersonUpdateView(LoginRequiredMixin, UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'main/create_person.html'

    def get_context_data(self, **kwargs):
        context = super(PersonUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Edytuj osobę'
        return context

class PersonDetailView(FormMixin, DetailView):
    model = Person
    template_name = 'main/detail_person.html'
    context_object_name = 'person'
    form_class = RateForm

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        context['form'] = RateForm(initial={'person': self.object})
        if self.request.user.is_authenticated:
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

class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    template_name = 'main/create_movie.html'
    form_class = MovieForm

    def get_context_data(self, **kwargs):
        context = super(MovieCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Stwórz film'
        return context

class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = ['title', 'description', 'date_of_realease', 'kind', 'actors', 'directors', 'scenarists']
    template_name = 'main/create_movie.html'

    def get_context_data(self, **kwargs):
        context = super(MovieUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Edytuj film'
        return context

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
        if Rate.objects.filter(movie=self.object, sender=self.request.user).exists():
            context['form'] = RateForm(
            initial={
            'movie': self.object,
            'choice': Rate.objects.filter(movie=self.object, sender=self.request.user).first().choice
            })
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if request.method == 'POST':
            if form.is_valid():
                new_rate, _ = Rate.objects.update_or_create(
                sender=self.request.user, 
                movie=self.object,
                defaults={'choice': form.cleaned_data['choice']}
            )
                return JsonResponse({'rate': model_to_dict(new_rate)}, status=200)
        else:
            return self.form_invalid(form)

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