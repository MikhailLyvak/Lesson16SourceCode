from django.urls import path

from .views import (
    index,
    ItemListView,
)

urlpatterns = [
    path("", index, name="index"),
    path("items/", ItemListView.as_view(), name="item-list")
]

app_name = "app_to_buy_list"
