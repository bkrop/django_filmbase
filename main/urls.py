from django.urls import path
from .views import PersonCreateView, PersonDetailView, MovieCreateView, MovieDetailView

urlpatterns = [
    path('person/create/', PersonCreateView.as_view(), name='create_person'),
    path('person/<slug:slug>/', PersonDetailView.as_view(), name='detail_person'),
    path('movie/create/', MovieCreateView.as_view(), name='create_movie'),
    path('movie/<slug:slug>/', MovieDetailView.as_view(), name='detail_movie'),    
]