from django.urls import path
from User import views
app_name="User"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),

    path('SearchProduct/',views.searchproduct,name="SearchProduct"),
    path('AjaxSubcategory/',views.ajaxsubcategory,name="ajaxsubcategory"),
    path('AddCart/<int:pid>',views.Addcart,name="AddCart"),
    path('Mycart/',views.Mycart,name="Mycart"),
    path('CartQty/',views.CartQty,name="CartQty"),
    path('DelCart/<int:did>',views.DelCart,name="DelCart"),
    path('payment/',views.payment,name="payment"),
    path('MyBookings/',views.MyBookings,name="MyBookings"),
    path('MyOrders/<int:wid>',views.MyOrders,name="MyOrders"),

    path('ajaxsearchpdt/',views.ajaxsearchpdt,name="ajaxsearchpdt"),
    path('ajaxFilter/',views.ajaxFilter,name="ajaxFilter"),
]