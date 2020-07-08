from django import forms
from .models import Rate, Person

class DateInput(forms.DateInput):
    input_type = 'date'

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ('choice',)

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['full_name', 'date_of_birth', 'avatar']
        widgets = {
            'date_of_birth': DateInput(),
        }