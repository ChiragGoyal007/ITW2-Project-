from django.shortcuts import render
from django.http import HttpResponse
from .models import Song, Library
from math import ceil 
from .forms import SearchForm
from django.db.models import Q
def index(request):
    songs = Song.objects.all()
    allsongs = []
    catprods = Song.objects.values('genre', 'id')
    cats = {item['genre'] for item in catprods}
    for cat in cats:
        song = Song.objects.filter(genre=cat)
        n = len(song)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allsongs.append([song, range(1, nSlides), nSlides])
    form = SearchForm()
    params = {'allsongs':allsongs, 'form': form}   
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return render(request,'shop/contact.html')

def SongView(request):
    return HttpResponse("Get your song details here")

def search(request):
    form = SearchForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            q = request.POST['query']
            obj = Song.objects.filter(Q(song_name__icontains=q)|Q(artist__icontains=q)|Q(genre__icontains=q)|Q(album__icontains=q))
    params = {'form': form, 'obj': obj}   
    return render(request,'shop/search.html',params)

def library(request):
    lib = Library.objects.all()
    return render(request,'shop/library.html', {'lib': lib})

def add_to_lib(request, id):
    message = None
    lib = Library.objects.all()
    try:
        obj = Song.objects.get(pk=id)
    except:
        obj = None
        message = "Song does not exist!"
        return render(request, 'shop/library.html', {'message': message, 'lib': lib})
    t, created = Library.objects.get_or_create(
        song_id = obj,
    )
    if created == False:
        message = "Song already in Library!"
        return render(request, 'shop/library.html', {'message': message, 'lib': lib})
    else:
        message = f"Song {obj.song_name} with ID {obj.pk} added to Library!"
    return render(request, 'shop/library.html', {'message': message, 'lib': lib})
