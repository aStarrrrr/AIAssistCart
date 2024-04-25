from django.db import models
from Administrator.models import *
from Guest.models import *

class tbl_product(models.Model):
    product_name=models.CharField(max_length=50)
    subcategory = models.ForeignKey(tbl_subcategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(tbl_brandname, on_delete=models.CASCADE)
    product_price=models.CharField(max_length=50)
    product_details=models.CharField(max_length=50)
    product_photo = models.FileField(upload_to='Assets/ProductPhoto/')
    sellerID=models.ForeignKey(tbl_seller,on_delete=models.CASCADE,null=True)

class tbl_productimages(models.Model):
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE,null=True)
    product_details=models.CharField(max_length=50)
    productimage_photo = models.FileField(upload_to='Assets/GallaryPhoto/')