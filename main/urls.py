from django.urls import path
from .views import PersonCreateView

urlpatterns = [
    path('person/create/', PersonCreateView.as_view(), name='create_person')
]