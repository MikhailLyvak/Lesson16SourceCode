from django.urls import path

from .views import (
    index,
    ItemListView,
    ItemCreateView,
    ItemUpdateView,
    ItemDetailView,
    delete_item,
    mark_item_as_bought
)

urlpatterns = [
    path("", index, name="index"),
    path("items/", ItemListView.as_view(), name="item-list"),
    path("items/create/", ItemCreateView.as_view(), name="item-create"),
    path("items/<int:pk>/update/", ItemUpdateView.as_view(), name="item-update"),
    path("items/<int:pk>/detail/", ItemDetailView.as_view(), name="item-detail"),
    path("items/<int:pk>/delete/", delete_item, name="item-delete"),
    path("items/<int:pk>/mark_as_bought/", mark_item_as_bought, name="mark-as-bought"),
]

app_name = "app_to_buy_list"
