from django.urls import path
from .views import (
    PersonCreateView,
    PersonDetailView,
    MovieCreateView,
    MovieDetailView,
    search,
    MovieListView,
    PersonUpdateView,
    MovieUpdateView
)

urlpatterns = [
    path('person/create/', PersonCreateView.as_view(), name='create_person'),
    path('person/<slug:slug>/', PersonDetailView.as_view(), name='detail_person'),
    path('movie/create/', MovieCreateView.as_view(), name='create_movie'),
    path('movie/<slug:slug>/', MovieDetailView.as_view(), name='detail_movie'),
    path('results', search, name='search'),
    path('movies/ranking/', MovieListView.as_view(), name='list_movie'),
    path('person/update/<slug:slug>/', PersonUpdateView.as_view(), name='update_person'),
    path('movie/update/<slug:slug>/', MovieUpdateView.as_view(), name='update_movie')
]