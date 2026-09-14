from django.db import models
from accounts.models import User
from foods.models import Food
# Create your models here.


class Items_Order(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    food = models.ForeignKey(Food, related_name='items', on_delete=models.CASCADE)
   

    def __str__(self):
        return f"Order Item {self.id}"

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Items_Order)


    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
