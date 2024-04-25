from django.db import models
from Guest.models import *
from Seller.models import *

class tbl_booking(models.Model):
    userID = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    booking_data = models.CharField(max_length=50)
    booking_amount = models.CharField(max_length=50)
    booking_status = models.IntegerField(default="0")

class tbl_cart(models.Model):
    productID = models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    cart_status = models.IntegerField(default="0")
    cart_quantity = models.IntegerField(max_length=50)
    bookingID = models.ForeignKey(tbl_booking,on_delete=models.CASCADE)

class tbl_history(models.Model):
    search_history = models.CharField(max_length=50)
    userID = models.ForeignKey(tbl_user, on_delete=models.CASCADE)