from django.db import models
from users.models import CustomUser


class ItemType(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    
    def __str__(self) -> str:
        return f"{self.name}"


class Item(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    discription = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField(null=False, blank=False)
    item_type = models.ForeignKey(
        ItemType, on_delete=models.CASCADE, null=False, blank=False
    )
    link = models.URLField(null=True, blank=True)
    bought_date = models.DateField(null=True, blank=True)
    is_bought = models.BooleanField(default=False)
    price_future = models.PositiveIntegerField(null=True, blank=True)
    created_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, null=False, blank=False
    )

    def __str__(self) -> str:
        return f"{self.name} -> {self.price} grn.  |  {self.item_type}"
