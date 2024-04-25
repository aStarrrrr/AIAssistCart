from django.db import models
from Administrator.models import *



class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    user_photo = models.FileField(upload_to='Assets/UserPhoto/')
    user_proof = models.FileField(upload_to='Assets/UserProof/')
    user_status = models.IntegerField(default="0")
    


class tbl_seller(models.Model):
    seller_name=models.CharField(max_length=50)
    seller_address=models.CharField(max_length=50)
    seller_contact=models.CharField(max_length=50)
    seller_email=models.CharField(max_length=50)
    seller_password=models.CharField(max_length=50)
    place = models.ForeignKey(tbl_place, on_delete=models.CASCADE)
    seller_photo = models.FileField(upload_to='Assets/SellerPhoto/')
    seller_proof = models.FileField(upload_to='Assets/SellerProof/')
    seller_status = models.IntegerField(default="0")
    