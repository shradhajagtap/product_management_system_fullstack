from django.db import models


class ProductOrder(models.Model):
    PAYMENT_CHOICE = [
    ("On", "ONLINE"),
    ("COD", "Cash on Delivery"),
    ]
    PRODUCT_QUANTITY = [("1", "One"), ("2", "Two"), ("3", "Three"), ("4", "Four"), ("5", "Five")]
    product_name = models.CharField(max_length=20)
    product_price = models.IntegerField()
    product_quan = models.CharField(max_length=10, choices=PRODUCT_QUANTITY)
    delivery_address = models.CharField(max_length=20)
    payment_mode = models.CharField(max_length=3, choices=PAYMENT_CHOICE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

