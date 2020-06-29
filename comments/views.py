from comments.models import Comment
from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from .models import Comment, Topic
from django.shortcuts import reverse
from main.models import Person, Movie
from django.db.models import Q

class TopicCreateView(CreateView):
    model = Topic
    fields = ['title', 'content']
    template_name = 'comments/create_topic.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        try:
            form.instance.person = Person.objects.get(slug=self.kwargs['slug'])
        except Person.DoesNotExist:
            form.instance.movie = Movie.objects.get(slug=self.kwargs['slug'])
        return super().form_valid(form)

class TopicDetailView(DetailView):
    model = Topic
    context_object_name = 'topic'
    template_name = 'comments/detail_topic.html'

    def get_object(self):
        topic = Topic.objects.get(
            Q(movie__slug=self.kwargs['slug'])|
            Q(person__slug=self.kwargs['slug'])
        )
        return topic