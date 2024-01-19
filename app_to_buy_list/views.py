from django.shortcuts import render
from django.views import generic

from .models import Item, ItemType

def index(request):
    num_item_types = ItemType.objects.count()
    num_item = Item.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_item": num_item,
        "num_item_types": num_item_types,
        "num_visits": num_visits + 1
    }

    return render(request, "app_to_buy_list/index.html", context=context)


class ItemListView(generic.ListView):
    model = Item
    template_name = "app_to_buy_list/item_list.html"
    context_object_name = "item_list"
