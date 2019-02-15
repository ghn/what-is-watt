from django.http import HttpResponseRedirect
from django.shortcuts import render

from app.watt.models import Item


def index(request):
    value = 0

    if request.method == 'POST':
        item1 = Item.objects.get(id=request.POST.get('item1'))
        item2 = Item.objects.get(id=request.POST.get('item2'))

        # compute conversion
        value = item1.id + item2.id

    return render(request, 'index.html', {
        'items': Item.objects.all(),
        'item1': item1,
        'item2': item2,
        'value': value
    })
