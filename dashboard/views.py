from django.shortcuts import render, get_object_or_404
from item .models import Item
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items,
    })

<<<<<<< HEAD
=======
@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
>>>>>>> fa57db1ec9d274e17ea09239e415a61b27f2d7a7
