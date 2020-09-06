from comments.models import Comment
from .models import Post
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import FormMixin
from comments.forms import CommentForm
from django.urls import reverse
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import render
from comments.models import Reply

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostListView(ListView):
    model = Post
    template_name = 'blog/homepage.html'
    context_object_name = 'posts'
    ordering = ['-date_of_create']

class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            if request.method == 'POST':
                new_comment = Comment.objects.create(
                    author = self.request.user,
                    post = self.object,
                    content = form.cleaned_data['content']
                )
                return JsonResponse({'comment': model_to_dict(new_comment)}, status=200)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.get_object()
        form.save()
        return super(PostDetailView, self).form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', kwargs={'slug': self.object.slug})

class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    context_object_name = 'post'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False

class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    context_object_name = 'post'
    fields = ['title', 'content']

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        else:
            return False

def post_comments(request, id):
    post = Post.objects.get(id=id)
    context = {'post': post}
    return render(request, 'blog/post_comments.html', context)

def comment_replies(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    replies = Reply.objects.filter(comment=comment)
    context = {'replies': replies}
    return render(request, 'blog/comment_replies.html', context)