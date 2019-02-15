from django.http import HttpResponseRedirect
from django.shortcuts import render

from app.watt.models import Item
from app.watt.lib import compute_energy


def index(request):
    if request.method == 'POST':
        item1 = Item.objects.get(id=request.POST.get('item1'))
        item2 = Item.objects.get(id=request.POST.get('item2'))
    else:
        item1 = Item.objects.first()
        item2 = Item.objects.last()

    value = compute_energy(item1, item2)

    return render(request, 'index.html', {
        'items': Item.objects.all(),
        'item1': item1,
        'item2': item2,
        'value': value
    })
