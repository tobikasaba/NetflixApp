from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Netflix

# Create your views here.


def index(request):
    netflix_genres = Netflix.objects.all()
    #output = ", ".join([n.sub_genre for n in netflix])
    # return HttpResponse(output)
    return render(request, "netflix/index.html", {"netflix_genres": netflix_genres})


def detail(request, netflix_id):
        netflix_genres = get_object_or_404(Netflix, pk=netflix_id)
        return render(request, "netflix/detail.html", { "netflix_genres": netflix_genres})
    