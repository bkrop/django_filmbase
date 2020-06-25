from comments.models import Comment
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Comment, Topic
from django.shortcuts import reverse
from main.models import Person, Movie

class TopicCreateView(CreateView):
    model = Topic
    fields = ['title', 'content']
    template_name = 'comments/create_topic.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        person = Person.objects.get(slug=self.kwargs['slug'])
        movie = Movie.objects.get(slug=self.kwargs['slug'])
        if person:
            form.instance.person = person
        form.instance.movie = movie
        return super().form_valid(form)
