from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse

from base.forms import RoomForm
from base.models import Room


# Create your views here.
def hello(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello, {s} Boy')

def search(request):
    q = request.GET.get('q', '')
    if (q==''):
        return HttpResponse("Nerozumím řeči tvého kmene!")
    rooms = Room.objects.filter(
        Q(name__contains=q) |                           #or nebo and - &
        Q(description__contains=q)
    )
    context = {'query': q, 'rooms': rooms}
    return render(request, "base/search.html", context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

class RoomView(ListView):
    template_name = 'base/rooms.html'
    model = Room

def roomCreate(request):
    # request.method == 'POST'
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms')
    # request.method == 'GET'
    form = RoomForm()
    context = {'form': form}
    return render(request, 'base/room_form.html', context)

