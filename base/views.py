from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse

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
