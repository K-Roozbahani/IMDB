from django.urls import path
from .views import movies_list, movies_detail

urlpatterns = [
    path('movies_list/', movies_list, name='movie_list'),
    path('movies_detail/<int:pk>/', movies_detail, name='movie_detail'),
]


