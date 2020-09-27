from django.views.generic import CreateView, DetailView, RedirectView
from .models import Comment, Topic
from django.shortcuts import reverse
from main.models import Person, Movie
from django.db.models import Q
from django.views.generic.edit import FormMixin
from .forms import CommentForm
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
import json


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

    def get_success_url(self):
        if self.__class__ == Movie:
            return reverse('detail_topic', kwargs={
                'topic_slug': self.object.slug,
                'slug': self.object.movie.slug
                })
        return reverse('detail_topic', kwargs={
                'topic_slug': self.object.slug,
                'slug': self.object.person.slug
                })

class TopicDetailView(FormMixin, DetailView):
    model = Topic
    context_object_name = 'topic'
    template_name = 'comments/detail_topic.html'
    form_class = CommentForm

    def get_object(self):
        topic = Topic.objects.filter(
            Q(movie__slug=self.kwargs['slug'])|
            Q(person__slug=self.kwargs['slug'])
        ).filter(slug=self.kwargs['topic_slug']).first()
        return topic

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'topic':self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.topic = self.get_object()
        form.save()
        return super(TopicDetailView, self).form_valid(form)

    def get_success_url(self):
        if self.__class__ == Movie:
            return reverse('detail_topic', kwargs={
                'topic_slug': self.object.slug,
                'slug': self.object.movie.slug
                })
        return reverse('detail_topic', kwargs={
                'topic_slug': self.object.slug,
                'slug': self.object.person.slug
                })

def like_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    user = request.user
    like = None
    if user not in comment.likes.all():
        comment.likes.add(user)
        like = True
    else:
        comment.likes.remove(user)
        like = False
    data = {
        'user': user.id,
        'comment': comment.id,
        'like': like
    }
    return HttpResponse(json.dumps(data))