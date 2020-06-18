from django.urls import path
from .views import PersonCreateView, PersonDetailView

urlpatterns = [
    path('person/create/', PersonCreateView.as_view(), name='create_person'),
    path('person/<int:pk>/', PersonDetailView.as_view(), name='detail_person')
]