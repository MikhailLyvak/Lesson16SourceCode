from django.urls import path

from .views import (
    index,
    ItemListView,
    ItemCreateView
)

urlpatterns = [
    path("", index, name="index"),
    path("items/", ItemListView.as_view(), name="item-list"),
    path("items/create/", ItemCreateView.as_view(), name="item-create"),
]

app_name = "app_to_buy_list"
