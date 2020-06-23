from main.models import Person, Rate
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DetailView
from .forms import RateForm
from django.views.generic.edit import FormMixin
from django.urls import reverse

class PersonCreateView(CreateView):
    model = Person
    fields = '__all__'
    template_name = 'main/create_person.html'

class PersonDetailView(FormMixin, DetailView):
    model = Person
    template_name = 'main/detail_person.html'
    context_object_name = 'person'
    form_class = RateForm

    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        context['form'] = RateForm(initial={'person': self.object})
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

