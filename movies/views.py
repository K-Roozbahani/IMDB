from django.shortcuts import render, get_object_or_404
from .models import Movie


def movies_list(request):
    limit = int(request.GET.get('limit', 8))
    offset = int(request.GET.get('offset', 0))
    movies = Movie.objects.all()[offset:limit]
    return render(request, 'movies_list.html', context={'movies': movies})gi


def movies_detail(request, pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=pk, is_valid=True)
        content = {'movie': movie}
        return render(request, 'movie_detail.html', context=content)
