from django.http import HttpResponse
from django.shortcuts import render

data = {
    "movies": [
        {
            'id': 5,
            'title': 'jaws',
            'year': 1669
        },
        {
            'id': 6,
            'title': 'sharknado',
            'year': 1600
        },
        {
            'id': 7,
            'title': 'The Meg',
            'year': 1669
        }
    ]
}


def movies(request):
    return render(request, 'movies/movies.html', data)


def home(request):
    return HttpResponse("Welcome to the home page")
