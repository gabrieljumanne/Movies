from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Movies, Users

# This is the general responce after making a requests....
# All the logic are done on the views


def movies(request):
    # Data inform of dictionary that will be passed in the the template
    data = Movies.objects.all()  # Here  i taking all the data objects
    Name = Users.objects.get(id=2)  # Here i am taking the users objects
    context = {
        'movies': data,
        'user': Name
    }
    # the render takes only three arguments....
    return render(request, 'movies/movies.html', context)


def home(request):
    return HttpResponse("Welcome to the home page")


def details(request, id):
    # querying each data by the id in database
    # Quaerying data from the movies table in the model taking the data that i want

    data = Movies.objects.get(pk=id)
    context_2 = {
        'movie': data
    }
    return render(request, 'movies/detail.html', context_2)


def add(request):
    # checking if the data has been submitted & create a movie object
    # Create the variable to hold an request data
    title = request.POST.get('title')
    year = request.POST.get('year')
    director = request.POST.get('director')

    if title and year and director:
        movie = Movies(title=title, year=year, director=director)
        movie.save()
        # After adding to the data base , redirect it to the list of database
        return HttpResponseRedirect('/movies/')
    return render(request, 'movies/add.html', )


def delete(request, id):
    try:
        movie = Movies.objects.get(pk=id).delete()
    except:
        raise Http404("This movie does not found")

    movie.delete()
    # re-direct the page after deleting.....
    return HttpResponseRedirect('/movies/')


# rendering template is used only when there is a need to uses
# that template
