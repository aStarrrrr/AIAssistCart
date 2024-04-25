from django.shortcuts import render,redirect
from Guest.models import *
from Seller.models import *
from User.models import *

def homepage(request):
    if 'uid' in request.session:
        return render(request,"User/HomePage.html")
    else:
        return redirect("Guest:Login")

def my_pro(request):
    if 'uid' in request.session:
        data=tbl_user.objects.get(id=request.session["uid"])
        return render(request,"User/MyProfile.html",{'data':data})
    else:
        return redirect("Guest:Login")

def editprofile(request):
    if 'uid' in request.session:
        prodata=tbl_user.objects.get(id=request.session["uid"])
        if request.method=="POST":
            prodata.user_name=request.POST.get('txtname')
            prodata.user_contact=request.POST.get('txtcon')
            prodata.user_email=request.POST.get('txtemail')
            prodata.save()
            return render(request,"User/EditProfile.html",{'msg':"Profile Updated"})
        else:
            return render(request,"User/EditProfile.html",{'prodata':prodata})
    else:
        return redirect("Guest:Login")

def changepassword(request):
    if 'uid' in request.session:
        if request.method=="POST":
            ccount=tbl_user.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcurpass')).count()
            if ccount>0:
                if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                    userdata=tbl_user.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcurpass'))
                    userdata.user_password=request.POST.get('txtnewpass')
                    userdata.save()
                    return render(request,"User/ChangePassword.html",{'msg':"Password Updated"})
                else:
                    return render(request,"User/ChangePassword.html",{'msg1':"Error in confirm Password"})
            else:
                return render(request,"User/ChangePassword.html",{'msg1':"Error in current password"})
        else:
            return render(request,"User/ChangePassword.html")
    else:
        return redirect("Guest:Login")
    

#Product Search
    
def ajaxsubcategory(request):
    if 'uid' in request.session:
        ctg = tbl_category.objects.get(id=request.GET.get("did"))
        subcategory = tbl_subcategory.objects.filter(category=ctg)
        return render(request,"User/AjaxSubcategory.html",{"subcategorydata":subcategory})
    else:
        return redirect("Guest:Login")
    
def searchproduct(request):
    if 'uid' in request.session:
        category = tbl_category.objects.all()
        brand = tbl_brandname.objects.all()
        productData=tbl_product.objects.all()
        if request.method=="POST":
            subcategorydata = tbl_subcategory.objects.get(id=request.POST.get('sel_subcategory'))
            if request.POST.get('sel_brand')!="":
                branddata = tbl_brandname.objects.get(id=request.POST.get('sel_brand'))
                productDatafilter=tbl_product.objects.filter(subcategory=subcategorydata,brand=branddata)
                return render(request,"User/ProductSearch.html",{"productdata":productDatafilter,"categorydata":category,"branddata":brand})
            elif request.POST.get('sel_category')!="":
                productDatafilter=tbl_product.objects.filter(brand=request.POST.get('sel_category'))
                return render(request,"User/ProductSearch.html",{"productdata":productDatafilter,"categorydata":category,"branddata":brand})
            else:
                productDatafilter=tbl_product.objects.filter(subcategory=subcategorydata)
                return render(request,"User/ProductSearch.html",{"productdata":productDatafilter,"categorydata":category,"branddata":brand})
        else:
            return render(request,"User/ProductSearch.html",{"categorydata":category,"branddata":brand,"productdata":productData})
    else:
        return redirect("Guest:Login")
    
def Addcart(request,pid):
    if 'uid' in request.session:
        productdata=tbl_product.objects.get(id=pid)
        user=tbl_user.objects.get(id=request.session["uid"])
        bookingcount=tbl_booking.objects.filter(userID=user,booking_status=0).count()
        if bookingcount>0:
         bookingdata=tbl_booking.objects.get(userID=user,booking_status=0)
         cartcount=tbl_cart.objects.filter(bookingID=bookingdata,productID=productdata).count()
         if cartcount>0:
          msg="Already added"
          return render(request,"User/ProductSearch.html",{'msg':msg})
         else:
          tbl_cart.objects.create(bookingID=bookingdata,productID=productdata,cart_quantity=1)
          msg="Added to Cart"
          return render(request,"User/ProductSearch.html",{'msg':msg})
        else:
           tbl_booking.objects.create(userID=user)
           bookingcount=tbl_booking.objects.filter(booking_status=0,userID=user).count()
           if bookingcount>0:
            bookingdata=tbl_booking.objects.get(userID=user,booking_status=0)
            cartcount=tbl_cart.objects.filter(bookingID=bookingdata,productID=productdata).count()
            if cartcount>0:
             msg="Already added"
             return render(request,"Customer/SearchShop.html",{'msg':msg})
            else:
             tbl_cart.objects.create(bookingID=bookingdata,productID=productdata,cart_quantity=1)
             return redirect("User:SearchProduct")
    else:
          return redirect("Guest:Login")
    
def Mycart(request):
    if 'uid' in request.session:
        if request.method=="POST":
            bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
            bookingdata.booking_amount=request.POST.get("carttotalamt")
            bookingdata.booking_status=1
            bookingdata.save()
            return redirect("User:payment")
        else:
            userdata=tbl_user.objects.get(id=request.session["uid"])
            bcount=tbl_booking.objects.filter(userID=userdata,booking_status=0).count()
        #cartcount=cart.objects.filter(booking__customer=customerdata,booking__status=0).count()
            if bcount>0:
                #cartdata=cart.objects.filter(booking__customer=customerdata,booking__status=0)
                book=tbl_booking.objects.get(userID=userdata,booking_status=0)
                bid=book.id
                request.session["bookingid"]=bid
                bkid=tbl_booking.objects.get(id=bid)
                cartdata=tbl_cart.objects.filter(bookingID=bkid)
                return render(request,"User/MyCart.html",{'cartdata':cartdata})
            else:
                return render(request,"User/MyCart.html")
    else:
        return redirect("Guest:Login")
       
    
def DelCart(request,did):
    if 'uid' in request.session:
        tbl_cart.objects.get(id=did).delete()
        return redirect("User:Mycart")
    else:
        return redirect("Guest:Login")
    
def CartQty(request):
    if 'uid' in request.session:
        qty=request.GET.get('QTY')
        cartid=request.GET.get('ALT')
        print(qty,cartid)
        cartdata=tbl_cart.objects.get(id=cartid)
        cartdata.cart_quantity=qty
        cartdata.save()
        return redirect("User:Mycart")
    else:
        return redirect("Guest:Login")

def payment(request):
    if 'uid' in request.session:
        if request.method == "POST":
            bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
            bookingdata.booking_status=2
            bookingdata.save()
            return redirect("User:SearchProduct")
        else:
            return render(request,"User/Payment.html")
    else:
        return redirect("Guest:Login")
   
def MyOrders(request,wid):
    if 'uid' in request.session:
        cartdata =tbl_cart.objects.filter(bookingID=wid)
        userdata=tbl_user.objects.get(id=request.session["uid"])
        bookingdata=tbl_booking.objects.filter(userID=userdata,booking_status=2)
        return render(request,"User/MyOrders.html",{'cartdata':cartdata,'bookingdata':bookingdata})
    else:
        return redirect("Guest:Login")

def MyBookings(request):
    if 'uid' in request.session:
        userdata=tbl_user.objects.get(id=request.session["uid"])
        bookingdata=tbl_booking.objects.filter(booking_status=2,userID=userdata)
        return render(request,"User/MyBookings.html",{'bookingdata':bookingdata})
    else:
        return redirect("Guest:Login")

def ajaxsearchpdt(request):
    if 'uid' in request.session:
        pdt  = tbl_product.objects.filter(product_name__istartswith=request.GET.get("key"))

        userdata=tbl_user.objects.get(id=request.session["uid"])
        tbl_history.objects.create(search_history=request.GET.get("key"),userID=userdata)

        return render(request,"User/AjaxKeySearch.html",{"data":pdt})
    else:
        return redirect("Guest:Login")
    
def ajaxFilter(request):
    category = request.GET.get("category")
    subcategory = request.GET.get("subcategory")
    brand = request.GET.get("brand")

    
    if category == "" and subcategory == "" and brand != "":
        bar = tbl_brandname.objects.get(id=brand)
        pdt  = tbl_product.objects.filter(brand=bar)
    elif subcategory != "" and brand == "":
        subcat = tbl_subcategory.objects.get(id=subcategory)
        pdt  = tbl_product.objects.filter(subcategory=subcat)
    elif subcategory != "" and brand != "":
        subcat = tbl_subcategory.objects.get(id=subcategory)
        bar = tbl_brandname.objects.get(id=brand)
        pdt  = tbl_product.objects.filter(subcategory=subcat,brand=bar)
    elif category != "" and subcategory == "" and brand == "":
        cat = tbl_category.objects.get(id=category)
        pdt  = tbl_product.objects.filter(subcategory__category=cat)

    return render(request,"User/AjaxKeySearch.html",{"data":pdt})
    

def logout(request):
    if 'uid' in request.session:
        del request.session["uid"]
        return redirect("Guest:Login")
    else:
        return redirect("Guest:Login")