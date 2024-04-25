from django.urls import path
from Seller import views
app_name="Seller"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),





    path('product/',views.product_details,name="product_details"),
    path('AjaxSubcategory/',views.ajaxsubcategory,name="ajaxsubcategory"),
    path('delproduct/<int:oid>',views.delproduct,name="delproduct"),


    path('vieworder/',views.vieworder,name="vieworder"),
    path('Myorders/<int:mid>',views.Myorders,name="Myorders"),


    path('ProductImages/',views.product_images,name="product_images"),
    path('Ajaxproduct/',views.ajaxproduct,name="ajaxproduct"),
]